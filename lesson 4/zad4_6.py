"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
 Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
 при котором повторение элементов списка будет прекращено.

"""
from sys import argv

script_name, starting_number, number_to_end_the_loop = argv


from itertools import count

for el in count(int(starting_number)):
    if el <= int(number_to_end_the_loop):
        print(f"{el} ")
    else:
        break

from itertools import cycle

my_list = [True, "ABC", 123456, None, 1.5]
c = 0
for el in cycle(my_list):
    if c < len(my_list):
        print(el)
        c +=1
    else:
        break



