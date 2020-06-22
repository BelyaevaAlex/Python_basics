"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f"{self.real} + {self.image} * i"

    def __add__(self, other):
        return f"{(self.real + other.real)} + {(self.image + other.image)}*i"

    def __mul__(self, other):
        return f"{(self.real * other.real - self.image * other.image)} + {(self.image * other.real + self.real * other.image)}*i"


# Проверка работы методов
complex_1 = ComplexNumber(2, 3)
complex_2 = ComplexNumber(5, -7)

assert complex_1 + complex_2 == "7 + -4*i"
assert complex_1 * complex_2 == "31 + 1*i"


