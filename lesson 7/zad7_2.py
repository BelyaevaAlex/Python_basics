"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod
#Абстрактный класс Одежда
class Clothes(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_s(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f"Общая площадь  ткани (общий подсчет расхода ткани) {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}")


# Класс Пальто
class Coat(Clothes):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = self.width / 6.5 + 0.5

    def __str__(self):
        return f"Площадь (расход ткани) на пальто {self.square_c}"


# Класс Костюм
class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = self.height * 2 + 0.3

    def __str__(self):
        return f"Площадь  (расход ткани) на костюм {self.square_s}"


coat = Coat(52, 1.6)
suit = Suit(52, 1.6)
clothes = Clothes(52, 1.6)
print(coat)
print(suit)
print(coat.get_square_c())
assert coat.get_square_c() == 8.5
print(suit.get_square_s())
assert suit.get_square_s() == 3.5
print(clothes.get_sq_full)

