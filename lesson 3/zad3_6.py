"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
def int_func(text):
    first_letter_small = text[0]
    """ Разделяем на случаи, чтобы отслеживать с какой буквы начинаются слова"""
    if (ord(first_letter_small)>=97 and ord(first_letter_small)<=122):
        first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
        return first_letter_big + text[1:]
    elif (ord(first_letter_small)>=65 and ord(first_letter_small)<=90):
        return text
    else:
        return str(text)
# Разбили строку по разделителю
text_string = input().split()
result = []
for text in text_string:
    # Добавляется int_func(text) в конец списка result
    result.append(int_func(text))
print(' '.join(result))
