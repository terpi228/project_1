from datetime import datetime
from src.services import search_by_date_range
from src.utils import reader_exel


def test_search():

    df = reader_exel('../data/TData.xls')

    start = datetime(2024, 1, 1)
    end = datetime(2024, 1, 31)

    result = search_by_date_range(df, start, end)
    print(f"Найдено {len(result)} транзакций")
    return result