"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import requests

def main():
    # url = "https://dl.dropboxusercontent.com/s/sipsmqpw1gwzd37/referat.txt"
    # response = requests.get(url)
    # content = response.content.decode('cp1251')
    # #content = response.text
    #
    # # запись контента в файл
    # with open("referat.txt", "w") as file:
    #     file.write(content)

    # открываем файл на чтение
    with open("referat.txt", "r") as file:
        content = file.read()

    # считаем количество символов
    length = len(content)
    print("Длина строки:", length)

    # считаем количество слов
    words = content.split()
    word_count = len(words)
    print("Количество слов:", word_count)

    # меняем точку на восклицательный знак
    new_content = content.replace(".", "!")

    # записываем новый файл с измененными данными
    with open("referat2.txt", "w") as file:
        file.write(new_content)

if __name__ == "__main__":
    main()
