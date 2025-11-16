import json
from datetime import datetime
import pandas as pd

from src.utils import reader_exel


def search_by_date_range(path, start_date, end_date):
    """
    Ищет транзакции в диапазоне дат в DataFrame
    """
    df = reader_exel(path)
    # Если даты в строковом формате, конвертируем их
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], format='%d.%m.%Y %H:%M:%S')

    # Создаем маску для фильтрации
    mask = (df['Дата операции'] >= start_date) & (df['Дата операции'] <= end_date)

    # Возвращаем отфильтрованный DataFrame
    return df[mask]



def simple_search(search_query: str, transactions_df):
    """простой поиск по одному слову"""


    query_lower = search_query.lower()

    mask = (transactions_df['Категория'].str.lower().str.contains(query_lower, na=False)|
            transactions_df['Описание'].str.lower().str.contains(query_lower, na=False ))

    result_df = transactions_df[mask]
    result_list = result_df.to_dict('records')


    return json.dumps(result_list, ensure_ascii=False, indent=2)


def transactions_for_person(transactions_df):
    """ищет транзакции межу пользователями"""
    is_transfer = transactions_df['Категория'].str.lower().str.contains('переводы', na=False)
    has_person_pattern = transactions_df['Описание'].str.contains(r'^\w+ [А-Яа-я]\.$', na=False)

    mask = is_transfer & has_person_pattern

    result_df = transactions_df[mask]
    result_list = result_df.to_dict('records')

    return json.dumps(result_list, ensure_ascii=False, indent=2)




if __name__ == "__main__":
    pass

