
"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn_right(self):
        print(f"Машина {self.name} повернула вправо")

    def turn_left(self):
        print(f"Машина{self.name} повернула влево")

    def show_speed(self):
        print(f"Текущая скорость машины {self.name} - {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость town car машины {self.name} -  {self.speed}")

        if self.speed > 40:
            print(f"Скорость машины {self.name} превышает допустимую для town car")
        else:
            print(f"Скорость машины {self.name} нормальна (допустима) для town car")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость work car машины {self.name} -  {self.speed}")

        if self.speed > 60:
            print(f"Скорость машины {self.name} превышает допустимую для work car")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print("Машина {self.name} является полицейской собственностью")
        else:
            print(f" Машина  {self.name} не является полицейской собственностью")

test_town_car = TownCar(100, "Красный", "Шевроле", False)
test_sport_car = SportCar(400, "Фиолетовый", "Ока", False)
test_work_car = WorkCar(70, "Белый", "Камаз", True)
test_police_car = PoliceCar(200, "Желтый", "Ауди", True)

test_town_car.go()
test_sport_car.stop()
test_work_car.turn_right()
assert test_police_car.is_police == True
assert test_town_car.is_police == False
assert test_work_car.speed == 70
assert test_sport_car.name == "Ока"
