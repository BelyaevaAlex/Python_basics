"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


# Класс Дата
class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_to_int(cls, date):

        try:
            new_date = date.split("-")
            day = int(new_date[0])
            month = int(new_date[1])
            year = int(new_date[2])
            return day, month, year
        except ValueError as err:
            return err

    @staticmethod
    def date_validation(date: str):
        day, month, year = Date.date_to_int(date)
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:

                    return f"Корректная дата"
                else:
                    return f"Некорректный год"
            else:
                return f"Некорректный месяц"
        else:
            return f"Некорректный день"


# Проверка методов
test_date = Date("22-06-2020")
day, month, year = Date.date_to_int(test_date.date)
assert day == 22
assert month == 6
assert year == 2020
assert test_date.date_validation("22-06-2020") == "Корректная дата"

test_date_2 = Date("32-06-2020")
day_2, month_2, year_2 = Date.date_to_int(test_date_2.date)
assert day_2 == 32
assert month_2 == 6
assert year_2 == 2020
assert test_date.date_validation("32-06-2020") == "Некорректный день"

test_date_3 = Date("22-13-2020")
day_3, month_3, year_3 = Date.date_to_int(test_date_3.date)
assert day_3 == 22
assert month_3 == 13
assert year_3 == 2020
assert test_date.date_validation("22-13-2020") == "Некорректный месяц"

test_date_4 = Date("22-06-2021")
day_4, month_4, year_4 = Date.date_to_int(test_date_4.date)
assert day_4 == 22
assert month_4 == 6
assert year_4 == 2021
assert test_date.date_validation("22-06-2021") == "Некорректный год"
