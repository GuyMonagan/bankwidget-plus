from bankwidget_plus.data_loader import load_data

def main():
    print("Hello, курсовая!")
    df = load_data("data/operations.xlsx")
    print(df.head())

if __name__ == "__main__":
    main()
