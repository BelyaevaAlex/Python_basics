"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх
4! = 1 * 2 * 3 * 4 = 24.
"""
from sys import argv
from itertools import count
from math import factorial

script_name, n = argv
n = int(n)
def fact(n):
    i=0
    for el in count(1):
        if i < n:
            yield factorial(el)
            i+=1
        else:
            break


for el in fact(n):
    print(f"{el}")
