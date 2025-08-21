from bankwidget_plus.data_loader import load_data
from bankwidget_plus.views import homepage_view
from bankwidget_plus.config import EXCEL_PATH

def main():
    df = load_data(EXCEL_PATH)
    date_input = input("Введите дату в формате DD.MM.YYYY HH:MM:SS: ")
    json_result = homepage_view(df, date_input)
    print(json_result)

if __name__ == "__main__":
    main()
