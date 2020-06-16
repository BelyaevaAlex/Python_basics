"""
4. Программа принимает действительное положительное число x и
целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
# Первый вариант решения
def my_func(x, y):
    """Программа принимает лишь действительное положительное число x и целое отрицательное число y """
    if (x > 0 and y < 0):
        return 1 / x ** abs(y)
    else:
        return "Программа принимает лишь действительное положительное число x и целое отрицательное число y."

# Второй вариант решения

def my_func_2(x, y):
    composition = 1
    if (x > 0 and y < 0):
        y = abs(y)
        for el in range(y):
            composition *= x
        return 1 / composition
    else:
        return "Программа принимает лишь действительное положительное число x и целое отрицательное число y."

while True:
    try:
        x = float(input("Введите действительное положительное число x "))
        y = int(input("Введите целое отрицательное число y, соответствующее степени "))
    except ValueError:
        print("Одно из чисел введено некорректно!")
        """ Чтобы была возможность ввести повторно """
        continue
    # Сравниваем результаты двух решений
    print(f"Результат функции возведения в степень с помощью оператора **: {my_func(x, y)}")
    print(f"Результат функции, реализуемой без оператора **, предусматривающей использование цикла умножения: {my_func_2(x, y)}")
    break

