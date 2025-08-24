# bankwidget-plus

Курсовой проект для анализа банковских транзакций.  
Приложение работает с Excel-файлом и предоставляет:

- Веб-функции для отображения и фильтрации транзакций
- Сервисы для поиска и анализа данных
- Отчёты по тратам в различных форматах

## Структура проекта

```commandline
.
├── src/
│ └── bankwidget_plus/
│ ├── main.py # Точка входа
│ ├── config.py # Конфигурация и переменные среды
│ ├── data_loader.py # Загрузка Excel-файла
│ ├── utils.py # Вспомогательные функции
│ ├── views.py # Веб-интерфейсы
│ ├── services.py # Сервисы (поиск, инвесткопилка и т.д.)
│ └── reports.py # Генерация отчётов
├── data/
│ └── operations.xlsx # Файл с транзакциями (по умолчанию)
├── tests/ # Тесты для всех модулей
├── .env # Переменные окружения (в .gitignore)
├── .env_template # Шаблон переменных
├── pyproject.toml # Poetry-конфигурация
└── README.md
```


## Установка

```
git clone https://github.com/GuyMonagan/bankwidget-plus.git
cd bankwidget-plus
poetry install
cp .env_template .env
```

## функциональность

```commandline
| Категория | Функция                         | Описание                       |
| --------- | ------------------------------- | ------------------------------ |
| Веб       | Главная страница (`homepage`)   | JSON-фильтр по дате            |
| Сервисы   | Простой поиск (`simple_search`) | Поиск по описанию транзакции   |
| Отчёты    | Траты по дням недели            | Группировка транзакций по дням |

```

## Тесты

```commandline
poetry run pytest --cov=src --cov-report=term-missing

```
Покрытие: ≥ 80%

Используются фикстуры, mock, patch, параметризация.


## Coverage Report

Локальный HTML-отчёт о покрытии кода доступен по пути:
http://localhost:63342/bankwidget-plus/htmlcov/index.html?_ijt=7s3lhrhnnja6lid01k1vlrgqj3&_ij_reload=RELOAD_ON_SAVE

## Линтинг и форматирование

```commandline
poetry run flake8 src/
poetry run black . --check
poetry run isort . --check
poetry run mypy src/

```

## Переменные окружения

Шаблон: `.env_template`

Ключевые переменные:

`EXCEL_PATH` — путь к `operations.xlsx`

`API_TOKEN` — токен для подключения к API (если потребуется)

## Примечания

Проект создан в рамках курса
