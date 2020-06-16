"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""

def my_func_division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Ошибка. Деление на ноль недопустимо!")


def my_func_division2(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Ошибка. Деление на ноль недопустимо!")

while True:
    try:
        num1 = int(input("Введите число, которое будет нашим делимым: "))
        num2 = int(input("Введите ненулевое число, которое будет нашим делителем: "))
    except ValueError:
        print("Одно из чисел введено некорректно!")
        """ Чтобы была возможность ввести повторно """
        continue
    # Сравниваем результаты двух решений
    print(f"{num1} / {num2} = {my_func_division(num1, num2)} ")
    print(f"{num1} / {num2} = {my_func_division2(num1, num2)} ")
    break
