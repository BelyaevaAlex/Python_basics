"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
"""
# Так как модуль os предоставляет широкий спектр функций для работы с файлами, используем именного его
import os
# Используем менеджер контекста
with open(os.path.join(os.getcwd(), "file_zad5_2.txt"), "r", encoding="utf8") as my_file:
    # Объявляю счетчик количества строк
    count_of_the_number_of_lines = 0
    for line in my_file:
        # Происходит подсчет слов методом split(), который разбивает строку на части, используя специальный разделитель, и возвращает эти части в виде списка
        count_of_the_number_of_words = len(line.split())
        count_of_the_number_of_lines += 1
        print(f"В строке {count_of_the_number_of_lines} количество слов: {count_of_the_number_of_words}")
    print(f"В файле {count_of_the_number_of_lines} строк")
