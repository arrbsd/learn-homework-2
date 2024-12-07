"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    # Текущую дата
    current_date = datetime.now()

    # Вчерашняя дата
    yesterday_date = current_date - timedelta(days=1)

    # Дата 30 дней назад
    days_ago = current_date - timedelta(days=30)

    # Напечатайте даты
    print("Вчера:", yesterday_date.date())
    print("Сегодня:", current_date.date())
    print("30 дней назад:", days_ago.date())


def str_2_datetime(date_string):
    date_format = "%d/%m/%y %H:%M:%S.%f"
    date_object = datetime.strptime(date_string, date_format)
    return date_object

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
