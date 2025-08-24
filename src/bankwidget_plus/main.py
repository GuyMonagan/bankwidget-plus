from bankwidget_plus.config import EXCEL_PATH
from bankwidget_plus.data_loader import load_data
from bankwidget_plus.views import homepage_view
from bankwidget_plus.reports import expenses_by_weekday
from bankwidget_plus.services import simple_search


def main() -> None:
    df = load_data(EXCEL_PATH)

    while True:
        print("\nВыберите действие:")
        print("1. Главная страница (фильтрация по дате)")
        print("2. Отчёт по дням недели")
        print("3. Простой поиск по описанию")
        print("0. Выход")
        choice = input("Ваш выбор (0/1/2/3): ").strip()

        if choice == "0":
            print("До свидания. 👋")
            break

        elif choice == "1":
            date_input = input("Введите дату в формате YYYY-MM-DD HH:MM:SS: ")
            json_result = homepage_view(df, date_input)
            print("\nРезультат:\n", json_result)

        elif choice == "2":
            start_date = input("Введите дату начала анализа (в формате YYYY-MM-DD): ")
            json_result = expenses_by_weekday(df, start_date)
            print("\nРезультат:\n", json_result)

        elif choice == "3":
            query = input("Введите строку для поиска по описанию: ")
            transactions = df.to_dict(orient="records")
            json_result = simple_search(query, transactions)
            print("\nРезультат:\n", json_result)

        else:
            print("Неверный выбор. Пожалуйста, введите 0, 1, 2 или 3.")


if __name__ == "__main__":
    main()
