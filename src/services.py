import os
import json
import math
import pandas as pd
from typing import List, Dict, Any
from datetime import datetime, timedelta


def search_by_date_range(transactions_df, days=5):
    """
    Фильтрует DataFrame по дате
    """
    transactions_df = pd.read_excel(transactions_df)
    df_copy = transactions_df.copy()

    today = datetime.now()
    start_date = today - timedelta(days=days)

    df_copy["Дата операции"] = pd.to_datetime(
        df_copy["Дата операции"], format="%d.%m.%Y %H:%M:%S"
    )

    mask = (df_copy["Дата операции"] >= start_date) & (
        df_copy["Дата операции"] <= today
    )

    return df_copy[mask]


def simple_search(search_query: str, transactions_df):
    """простой поиск по одному слову"""

    query_lower = search_query.lower()

    mask = transactions_df["Категория"].str.lower().str.contains(
        query_lower, na=False
    ) | transactions_df["Описание"].str.lower().str.contains(query_lower, na=False)

    result_df = transactions_df[mask]
    result_list = result_df.to_dict("records")

    return json.dumps(result_list, ensure_ascii=False, indent=2)


def transactions_for_person(transactions_df):
    """ищет транзакции межу пользователями"""
    is_transfer = (
        transactions_df["Категория"].str.lower().str.contains("переводы", na=False)
    )
    has_person_pattern = transactions_df["Описание"].str.contains(
        r"^\w+ [А-Яа-я]\.$", na=False
    )

    mask = is_transfer & has_person_pattern

    result_df = transactions_df[mask]
    result_list = result_df.to_dict("records")

    return json.dumps(result_list, ensure_ascii=False, indent=2)


def phone_search(input_data):
    """Ищет ВСЕ транзакции с телефонными номерами"""
    try:
        if isinstance(input_data, str):
            if not os.path.exists(input_data):
                return {"error": f"Файл не найден: {input_data}"}
            try:
                input_data = pd.read_excel(input_data)
            except Exception:
                try:
                    input_data = pd.read_csv(input_data)
                except Exception as e:
                    return {"error": f"Не удалось прочитать файл: {e}"}

        # Проверка на df
        if not hasattr(input_data, "empty"):
            return {"error": "Ожидался DataFrame или путь к файлу"}

        df = input_data

        if df.empty:
            return {"error": "Пустой DataFrame"}

        if "Описание" not in df.columns:
            return {"error": "Колонка 'Описание' не найдена"}

        patterns = [
            r"\+\d{1,3}[\s-]?\(?\d{1,5}\)?[\s-]?\d{1,5}[\s-]?\d{1,5}[\s-]?\d{1,5}",
            r"8[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}",
            r"7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}",
        ]

        combined_pattern = "|".join(f"(?:{p})" for p in patterns)
        mask = df["Описание"].str.contains(combined_pattern, na=False, regex=True)
        descriptions = df.loc[mask, "Описание"].tolist()

        return {"data": descriptions}

    except Exception as e:
        return {"error": f"Ошибка поиска: {e}"}


def round_to_next(val: float, step: int) -> float:
    return math.ceil(abs(val) / step) * step


def parse_amount(amount_str):
    """Преобразует строку с суммой в число"""
    if isinstance(amount_str, (int, float)):
        return float(amount_str)
    return float(amount_str.replace(" ", "").replace(",", "."))


def sort_to_data(month: str, transactions_df: List[Dict[str, Any]]):
    df = pd.DataFrame(transactions_df)

    df["Дата операции"] = pd.to_datetime(
        df["Дата операции"], format="%d.%m.%Y %H:%M:%S"
    )

    target_date = datetime.strptime(month, "%Y-%m")

    monthly_data = df[
        (df["Дата операции"].dt.year == target_date.year)
        & (df["Дата операции"].dt.month == target_date.month)
    ]

    return monthly_data


def investment_bank(
    month: str, transactions_df: List[Dict[str, Any]], limit: int
) -> float:
    monthly_data = sort_to_data(month, transactions_df)

    savings = 0
    for amount in monthly_data["Сумма операции"]:
        if amount < 0:
            rounded = round_to_next(amount, limit)
            savings += rounded - abs(amount)

    return round(savings)


if __name__ == "__main__":

    df = pd.read_excel("../data/TData.xls")
    transactions = df.to_dict("records")

    result = investment_bank("2025-08", transactions, 50)
    print(result)
