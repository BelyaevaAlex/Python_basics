"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

# Класс-исключение, обрабатывающий ситуацию деления но ноль
class DivisionByZeroError(Exception):
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return(f"Ошибка. Деление невозможно!")

print(DivisionByZeroError.divide_by_null(10, 2000))
print(DivisionByZeroError.divide_by_null(10, 0.5))
print(DivisionByZeroError.divide_by_null(10, 0))


