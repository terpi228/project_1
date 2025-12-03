from src.services import search_by_date_range
import datetime
import requests
import json





def main_page(date):
    """Вывод JSON Ответа в виде:
   1.  Утро/день/вечер/ночь в зависимости от текущего времени.
   2.  Поиск по всему Excel-файлу.
   4.  Остаток по счету.
   5.  Кешбэк."""
    current_date_time = datetime.datetime.now()
    if current_date_time.hour < 6 or 12 < current_date_time.hour:
        greeting = "Доброе утро"
    elif current_date_time.hour < 12 or 18 < current_date_time.hour:
        greeting = "Добрый день"
    elif current_date_time.hour < 18 or 24 < current_date_time.hour:
        greeting = "Добрый вечер"
    elif current_date_time.hour < 0 or 6 < current_date_time.hour:
        greeting = "Доброй ночи"


    return greeting


if __name__ == "__main__":
    result = main_page("2025-08-14 12:00:11")
    print(result)
    print(type(result))