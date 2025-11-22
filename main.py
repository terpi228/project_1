from src.services import investment_bank, phone_search
import time
import os


def clear():
    return os.system("cls" if os.name == "nt" else "clear")


def demonstration():
   try:
        while True:
            clear()
            print("╔════════════════════════════╗")
            print("║  ДЕМОНСТРАЦИОННАЯ ВЕРСИЯ   ║")
            print("╠════════════════════════════╣")
            print("║ 1. Веб страницы            ║")
            print("║ 2. Сервисы                 ║")
            print("║ 3. Отчеты                  ║")
            print("║ 4. Поиск по номеру         ║")
            print("║ 0. q                       ║")
            print("╚════════════════════════════╝")

            user = int(input())
            if user == 1:
                clear()
                print("Функция в рвзработке")
                input("Нажмите Enter чтобы продолжить...")

            elif user == 2:
                print("Функция в рвзработке")
                input("Нажмите Enter чтобы продолжить...")

            elif user == 4:
                clear()
                time.sleep(2)
                res = phone_search("data/TData.xls")
                print(res)
                input("\nНажмите Enter чтобы продолжить...")
                clear()

            elif user == 0:
                print("Завершение программы")
                break
   except Exception as e:
       print(F"Причина {e}")

if __name__ == "__main__":
    demonstration()
