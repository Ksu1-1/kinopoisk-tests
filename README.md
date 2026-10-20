# kinopoisk-tests
Дипломная работа: автоматизация тестирования Кинопоиск

# Автоматизированные тесты для Кинопоиска

## Описание проекта

Проект содержит набор автоматизированных тестов для сайта **Кинопоиск** (kinopoisk.ru) и его публичного API. Включает функциональные, негативные и контрактные тесты, покрывающие ключевые пользовательские сценарии.

## Технологии

- **Python 3.14**
- **pytest** — фреймворк для запуска тестов
- **Playwright** — UI-автоматизация 
- **requests** — HTTP-запросы для API-тестов
- **Allure** — генерация отчётов
- **Black** — автоформатирование кода
- **flake8** — статический анализ кода

## Структура проекта

    kinopoisk-tests/
    ├── api/                        # Хелпер для работы с API
    │   └── kinopoisk_api.py
    ├── pages/                      # Page Object модели
    │   ├── base_page.py
    │   ├── main_page.py
    │   ├── movie_page.py
    │   └── search_results_page.py
    ├── test/
    │   ├── api/                    # 5 API-тестов
    │   │   ├── test_movie_search.py
    │   │   ├── test_movie_by_id.py
    │   │   ├── test_filter.py
    │   │   ├── test_no_auth.py
    │   │   └── test_invalid_id.py
    │   ├── ui/                     # 5 UI-тестов
    │   │   ├── test_search.py
    │   │   ├── test_person_search.py
    │   │   ├── test_movie_card.py
    │   │   ├── test_sort_by_rating.py
    │   │   └── test_filter_genre_country.py
    │   └── conftest.py             # Фикстуры pytest
    ├── allure-results/             # Сырые данные Allure
    ├── allure-report/              # Сгенерированный HTML-отчёт
    ├── test_data.json              # Конфигурация и тестовые данные
    ├── requirements.txt            # Зависимости проекта
    ├── .flake8                     # Настройки flake8
    └── pyproject.toml              # Настройки Black

## Быстрый старт

### 1. Установка зависимостей

    py -m pip install -r requirements.txt

### 2. Запуск всех тестов

    py -m pytest test/ -v

### 3. Запуск только API-тестов

    py -m pytest test/api/ -v

### 4. Запуск только UI-тестов

    py -m pytest test/ui/ -v

### 5. Генерация отчёта Allure

    allure generate allure-results -o allure-report --clean
    allure open allure-report

### 6. Проверка качества кода

    py -m black .
    py -m flake8 .

## Что покрыто тестами

### API-тесты (5 штук)

| № | Тест | Тип | Что проверяет |
|---|------|-----|---------------|
| 1 | test_search_movie_by_name | Позитивный | Поиск фильма по названию |
| 2 | test_get_movie_by_id | Позитивный | Получение фильма по ID |
| 3 | test_filter_by_genre_and_country | Позитивный | Фильтрация по жанру и стране |
| 4 | test_search_without_auth | Негативный | Защита API без токена |
| 5 | test_get_movie_with_invalid_id | Негативный | Обработка невалидного ID |

### UI-тесты (5 штук)

| № | Тест | Что проверяет |
|---|------|---------------|
| 1 | test_search_movie_by_name | Поиск фильма через UI |
| 2 | test_search_person_by_name | Поиск персоны через UI |
| 3 | test_open_movie_card | Открытие карточки фильма |
| 4 | test_sort_movies_by_rating | Сортировка по рейтингу |
| 5 | test_filter_genre_and_country | Фильтрация по стране |

## Конфигурация

Все тестовые данные (URL, API-ключ, поисковые запросы) вынесены в файл `test_data.json`. Это позволяет легко переключаться между окружениями (prod/stage/local), меняя только конфиг.

## Архитектурные решения

- **Page Object Model** — локаторы и действия инкапсулированы в классах `pages/`, что делает тесты поддерживаемыми
- **Helper Class** — логика API-запросов вынесена в `KinopoiskAPI`, реализует принцип DRY
- **Фикстуры pytest** — переиспользуемая инициализация браузера и API-клиента через `conftest.py`
- **Явные ожидания** — `wait_for(state="visible")` вместо `time.sleep()` для стабильности
- **Allure-шаги** — `@allure.step` для читаемых отчётов с бизнес-логикой

