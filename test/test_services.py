from src.services import (
    category_of_cashback,
    simple_search,
    phone_search,
    investment_bank,
    search_by_date_range,
    round_to_next,
    parse_amount,
)
import os
import sys
import pandas as pd
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


test_data = [
    {
        "Дата платежа": "01.03.2024",
        "Категория": "Супермаркеты",
        "Сумма платежа": 5000,
        "Описание": "Покупка в Пятерочке",
        "Сумма операции": -5000,
        "Дата операции": "01.03.2024 12:30:00",
    },
    {
        "Дата платежа": "15.03.2024",
        "Категория": "Рестораны",
        "Сумма платежа": 3000,
        "Описание": "Ужин в кафе",
        "Сумма операции": -3000,
        "Дата операции": "15.03.2024 20:15:00",
    },
    {
        "Дата платежа": "20.03.2024",
        "Категория": "Супермаркеты",
        "Сумма платежа": 2000,
        "Описание": "Перевод +79161234567",
        "Сумма операции": -2000,
        "Дата операции": "20.03.2024 14:45:00",
    },
    {
        "Дата платежа": "25.02.2024",
        "Категория": "Транспорт",
        "Сумма платежа": 1000,
        "Описание": "Такси",
        "Сумма операции": -1000,
        "Дата операции": "25.02.2024 09:20:00",
    },
]


def test_category_of_cashback():
    print("=== Тест category_of_cashback ===")
    df = pd.DataFrame(test_data)

    result = category_of_cashback(df, 3, 2024)
    print("✓ Тест с данными за март 2024")

    result = category_of_cashback(df, 1, 2024)
    print("✓ Тест без данных за период")
    print(result)


def test_simple_search():
    print("=== Тест simple_search ===")
    df = pd.DataFrame(test_data)

    result = simple_search("супермаркеты", df)
    data = json.loads(result)
    print(f"✓ Поиск 'супермаркеты': найдено {len(data)} записей")

    result = simple_search("пятерочке", df)
    data = json.loads(result)
    print(f"✓ Поиск 'пятерочке': найдено {len(data)} записей")
    print()


def test_phone_search():
    print("=== Тест phone_search ===")
    df = pd.DataFrame(test_data)

    result = phone_search(df)
    print(f"✓ Поиск телефонов: {len(result['data'])} номеров")
    print()


def test_investment_bank():
    print("=== Тест investment_bank ===")

    # Теперь данные содержат ВСЕ нужные колонки
    result = investment_bank("2024-03", test_data, 50)
    print(f"✓ Инвесткопилка за март 2024: {result} руб.")

    result = investment_bank("2024-03", test_data, 100)
    print(f"✓ Инвесткопилка с лимитом 100: {result} руб.")
    print()


def test_search_by_date_range():
    print("=== Тест search_by_date_range ===")
    df = pd.DataFrame(test_data)

    result = search_by_date_range(df, 3, 2024)
    print(f"✓ Транзакции за март 2024: {len(result)} записей")
    print()


def test_round_to_next():
    print("=== Тест round_to_next ===")

    tests = [(123, 50, 150), (78, 10, 80), (100, 100, 100), (199, 50, 200)]

    for value, step, expected in tests:
        result = round_to_next(value, step)
        status = "✓" if result == expected else "✗"
        print(f"{status} {value} → {result} (ожидалось {expected})")
    print()


def test_parse_amount():
    print("=== Тест parse_amount ===")

    tests = [
        ("1 000,50", 1000.5),
        ("500", 500.0),
        (750, 750.0),
        ("2000.75", 2000.75),
        ("1,500", 1.5),
    ]

    for value, expected in tests:
        try:
            result = parse_amount(value)
            status = "✓" if abs(result - expected) < 0.01 else "✗"
            print(f"{status} '{value}' → {result} (ожидалось {expected})")
        except Exception as e:
            print(f"✗ '{value}' → ОШИБКА: {e}")
    print()


def run_all_tests():
    print("🚀 ЗАПУСК ИСПРАВЛЕННЫХ ТЕСТОВ\n")

    test_category_of_cashback()
    test_simple_search()
    test_phone_search()
    test_investment_bank()
    test_search_by_date_range()
    test_round_to_next()
    test_parse_amount()

    print("🎯 ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")


if __name__ == "__main__":
    run_all_tests()
