"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    data = [
        {"name": "Миша", "age": 36, "job": "Инженер"},
        {"name": "Юля", "age": 24, "job": "Бухгалтер"},
        {"name": "Вика", "age": 29, "job": "Проектировщик"},
        {"name": "Кирилл", "age": 31, "job": "Зам генерального директора"}
    ]

    # записываем в файл данные, разделенные точкой с запятой
    with open("data.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "job"], delimiter=";")
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    main()
