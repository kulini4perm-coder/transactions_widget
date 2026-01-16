from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import get_financial_transactions
from src.data_loader import read_transactions_from_csv, read_transactions_from_excel
from src.widget import mask_account_card, get_date


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    # 1. Загрузка данных
    transactions = []
    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = get_financial_transactions("data/operations.json")
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = read_transactions_from_csv("data/transactions.csv")
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = read_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор меню.")
        return

    # 2. Фильтрация по статусу
    while True:
        status = (
            input(
                "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )

        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, status)
            print(f'Программа: Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Программа: Статус операции "{status}" недоступен.')

    # 3. Сортировка по дате
    is_sort = input("\nОтсортировать операции по дате? Да/Нет\n").strip().lower()
    if is_sort == "да":
        while True:
            order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
            if "возраст" in order:
                transactions = sort_by_date(transactions, descending=False)
                break
            elif "убыв" in order:
                transactions = sort_by_date(transactions, descending=True)
                break
            else:
                print("Программа: Пожалуйста, введите 'по возрастанию' или 'по убыванию'.")

    # 4. Фильтрация по валюте
    is_rub = input("\nВыводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if is_rub == "да":
        transactions = [
            t
            for t in transactions
            if t.get("currency_code") == "RUB"
            or (t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB")
        ]

    # 5. Фильтрация по слову
    is_search = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if is_search == "да":
        search_word = input("Введите слово для поиска: ")
        transactions = process_bank_search(transactions, search_word)

    # 6. Вывод результата
    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")

    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия.")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")
        for op in transactions:
            # Форматируем дату
            raw_date = op.get("date", "")
            if raw_date:
                date = get_date(raw_date)
            else:
                date = "00.00.0000"

            # Маскируем данные отправителя и получателя
            from_info = str(op.get("from", ""))
            to_info = str(op.get("to", ""))

            # Формируем строку с замаскированными данными
            if from_info:
                from_masked = mask_account_card(from_info)
                to_masked = mask_account_card(to_info)
                transfer_line = f"{from_masked} -> {to_masked}"
            else:
                # Если отправителя нет (например, открытие вклада)
                transfer_line = mask_account_card(to_info) if to_info else "Счет не указан"

            desc = op.get("description", "Без описания")
            amount = op.get("amount") or op.get("operationAmount", {}).get("amount")
            amount = int(float(amount))
            curr = op.get("currency_code") or op.get("operationAmount", {}).get("currency", {}).get("code")

            # Выводим транзакции в нужном формате
            print(f"{date} {desc}")
            print(transfer_line)
            print(f"Сумма: {amount} {curr}\n")


if __name__ == "__main__":
    main()
