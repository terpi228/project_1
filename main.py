import json

import pandas as pd
from pandas import read_excel

from src.services import (
    investment_bank,
    phone_search,
    simple_search,
    category_of_cashback,
)
import os

from src.utils import reader_exel


def clear():
    return os.system("cls" if os.name == "nt" else "clear")

def demonstration_servis():
    try:
        while True:
            clear()

            print('''
            ╔════════════════════════════╗
            ║ 1.Выгодные категории.      ║
            ║ 2.Инвесткопилка            ║
            ║ 3.Простой поиск            ║
            ║ 4.Поиск по номеру          ║
            ║ 0.Выход                    ║
            ╚════════════════════════════╝
                ''')

            user = int(input())
            if user == 1:
                try:
                    user_month = int(input("введите месяц: "))
                    user_yera = int(input("введите год: "))
                    df = pd.read_excel("data/operations.xls")

                    print(f"Загружено {len(df)} транзакций")

                    result = category_of_cashback(df, user_month, user_yera)
                    print(result)

                except FileNotFoundError:
                    print("Ошибка: файл ../data/operations.xls не найден")
                except Exception as e:
                    print(f"Что-то пошло не так: {e}")
                input("Нажмите Enter чтобы продолжить...")

            elif user == 2:

                df = read_excel("data/operations.xls")
                result_2 = investment_bank("2025-06", df, 50)
                print(
                    f"8-2025 в этом месяце пользователь отложил бы в инвест копилку: {result_2}"
                )
                input("Нажмите Enter чтобы продолжить...")

            elif user == 3:
                clear()
                query = input("Введите слово для поиска: ")

                df = reader_exel("data/operations.xls")
                result_3 = simple_search(query, df)

                parsed = json.loads(result_3)

                print(f"Найдено: {len(parsed)} записей")
                print(json.dumps(parsed[:10], ensure_ascii=False, indent=2))

                input("Нажмите Enter чтобы продолжить...")

            elif user == 4:
                res = phone_search("data/operations.xls")
                print(res)
                input("\nНажмите Enter чтобы продолжить...")
                clear()

            elif user == 0:
                print("Завершение программы")
                break
    except Exception as e:
        print(f"Причина {e}")


def demonstration_views():
    while True:
        clear()

        print('''
╔════════════════════════════╗
║ 1. Страница «Главная»      ║
║ 2. Страница «События»      ║
╚════════════════════════════╝
            ''')

        user = int(input())
        if user == 1:
            pass

        elif user == 0:
            print("Завершение программы")
            break

def demonstration_reports():
    while True:
        clear()

        print('''
╔═══════════════════════════════╗
1. Траты по категориям
2. Траты по дням недели
3. Траты в рабочий/выходной день
╚═══════════════════════════════╝
            ''')
        user = int(input())
        if user == 1:
            pass

        elif user == 0:
            print("Завершение программы")
            break


def menu_selection():
    clear()
    print('''
╔════════════════════════════╗
║  ДЕМОНСТРАЦИОННАЯ ВЕРСИЯ   ║
╚════════════════════════════╝
1 - Веб-страницы
2 - Сервисы
3 - Отчеты
          ''')
    user = int(input('Ввод: '))
    if user == 1:
        demonstration_views()
    elif user == 2:
        demonstration_servis()
    elif user == 3:
        demonstration_reports()


if __name__ == "__main__":
    menu_selection()
