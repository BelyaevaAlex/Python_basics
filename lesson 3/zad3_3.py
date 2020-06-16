"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(num1, num2, num3):
    return max(num1, num2) + max(num1, num3)

def my_func2(num1, num2, num3):
    """ Объявление списка из наших аргументов """
    num_list = [num1, num2, num3]
    num_list.remove(min(num1, num2, num3))
    return sum(num_list)

while True:
    try:
        num1 = int(input("Введите первый аргумент"))
        num2 = int(input("Введите второй аргумент"))
        num3 = int(input("Введите третий аргумент"))
    except ValueError:
        print("Один из аргументов введен некорректно!")
        """ Чтобы была возможность ввести повторно """
        continue
    # Сравниваем результаты двух решений
    print(f"{my_func(num1, num2, num3)}")
    print(f"{my_func2(num1, num2, num3)}")
    break
