"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class ValidationError(Exception):
    def __init__(self, txt):
        self.txt = txt


# Класс «Склад оргтехники»
class OfficeEquipmentStore:
    def __init__(self):

        self.office_equipment_dict = {}

    def add_to_store(self, *args):

        for equipment in args:
            # Проверка, что переданный аргумент относится к классу OfficeEquipment
            if isinstance(equipment, OfficeEquipment):
                # Добавление аргументов объекта в словарь
                original_vars = vars(equipment)
                # Создание копии словаря original_vars, т.к. в дальнейшем придется удалять элементы из неё
                temp_copy_vars = original_vars.copy()
                # Флаг того, что запись с такими данными отсутствует в словаре
                copy_flag = False
                # Удаляем имя оргтехники (Принтер, Сканер, Ксерокс) из словаря
                name = temp_copy_vars.pop("name")
                # Удаляем количество оргтехники из словаря объекта
                number = temp_copy_vars.pop("number")
                # Проверяем, что тип оргтехники присутствует в результирующем словаре. Если нет - добавить ключ и запись по нему
                if name in self.office_equipment_dict.keys():
                    # Обходим каждую запись по этому типу для проверки
                    for dict_rec in self.office_equipment_dict[name]:
                        # Создаем копию словаря каждой записи
                        temp_dict = dict_rec.copy()
                        # Удаляем из временной копии словаря количество
                        temp_dict.pop("number")
                        # Сравниваем временные копии без name и number
                        if temp_copy_vars == temp_dict:
                            # Если запись с такими данными уже присутствует,  то меняем лишь  количество таких объектов на складе
                            dict_rec["number"]["склад"] += number
                            # Переключаем флаг
                            copy_flag = not copy_flag
                            break
                    # Если флаг показывае, что отсутствует запись, то добавляем её
                    if not copy_flag:
                        temp_copy_vars.update({"number": {"склад": number}})
                        self.office_equipment_dict[name].append(temp_copy_vars)
                else:
                    temp_copy_vars.update({"number": {"склад": number}})
                    self.office_equipment_dict.update({name: [temp_copy_vars]})

    def add_to_unit(self, unit, *args):

        for equipment in args:
            # Проверка, что переданный аргумент относится к классу OfficeEquipment
            if isinstance(equipment[0], OfficeEquipment):
                # Сборка словаря из аргументов объекта
                equipment_vars = vars(equipment[0])
                # Сохраняем количество, которое необходимо передать в number
                number = equipment[1]
                # Создание копии словаря equipment_vars, т.к. не хотим «портить» основной  и будем удалять элементы из копии
                temp_equipment_vars = equipment_vars.copy()
                temp_equipment_vars.pop("number")
                temp_equipment_vars.pop("name")
                # Проверяем, что тип оргтехники присутствует в результирующем словаре. Если нет - запись пропускается
                if equipment_vars["name"] in self.office_equipment_dict:
                    # Обходим каждую запись по этому типу для проверки
                    for dict_rec in self.office_equipment_dict[equipment_vars["name"]]:
                        # Создаем копию словаря каждой записи
                        temp_dict_rec = dict_rec.copy()
                        temp_dict_rec.pop("number")
                        # Сравниваем временные копии без name и number
                        if temp_equipment_vars == temp_dict_rec:
                            # Если подразделения нет в словаре данного типа в "Количество" данного типа оргтехники, то добавляем туда ключ
                            if not unit in dict_rec["number"]:
                                dict_rec["number"].update({unit: 0})
                            try:
                                # Если на складе меньше количество объектов, чем указано для переноса, то попадаем в исключение ValidationError
                                if not (dict_rec["number"]["склад"] - number > 0):
                                    raise ValidationError(f"Недостаточно экземпляров техники {equipment_vars['name']} с характеристиками {temp_equipment_vars} на складе для передачи в подразделение!")
                                    # Если ошибок нет, добавляем количество объектов к количеству в подразделении, а со склада отнимаем
                                    dict_rec["number"][unit] += number
                                    dict_rec["number"]["склад"] -= number
                            except ValidationError as err:
                                print(err)
                            break
                else:
                    continue

    def get_all_equipment(self):
        return self.office_equipment_dict


# Базовый класс «Оргтехника»
class OfficeEquipment:
    def __init__(self, number, model):
        self.number = number
        self.model = model

    # Функция-декоратор для проверки ожидаемых типов
    def typecheck(types):
        def __f(f):
            def _f(*args):
                # Функция zip объединяет в кортежи элементы из последовательностей переданных в качестве аргументов, возможно, так как кортежи подаются одной длины
                for a, t in zip(args, types):
                    if not isinstance(a, t):
                        raise ValidationError(f"Вместо ожидаемого {t} получено: {a}")
                return f(*args)

            return _f

        return __f


# Класс Принтер
class Printer(OfficeEquipment):
    @OfficeEquipment.typecheck(types=[OfficeEquipment, int, str, str])
    def __init__(self, number, model, type):
        super().__init__(number, model)
        self.name = "Принтер"
        self.type = type


# Класс Сканер,
class Scanner(OfficeEquipment):

    @OfficeEquipment.typecheck(types=[OfficeEquipment, int, str, str])
    def __init__(self, number, model, scan_resolution):
        self.name = "Сканер"
        super().__init__(number, model)
        self.scan_resolution = scan_resolution


# Класс Ксерокс
class Copier(OfficeEquipment):
    @OfficeEquipment.typecheck(types=[OfficeEquipment, int, str, int])
    def __init__(self, number, model, copy_color_depth):
        self.name = "Ксерокс"
        super().__init__(number, model)
        self.copy_color_depth = copy_color_depth


# Проверка методов
printer_1 = Printer(5, "HP", "струйный")
printer_2 = Printer(7, "HP", "струйный")
printer_3 = Printer(5, "COPIER", "матричный")
printer_4 = Printer(8, "COPIER", "матричный")
printer_5 = Printer(9, "HP", "струйный")
scanner_1 = Scanner(5, "COPIER", "1440 * 1440")
copier_1 = Copier(15, "CANON", 36)
copier_2 = Copier(7, "HP", 16)
copier_3 = Copier(25, "CANON", 96)
store = OfficeEquipmentStore()
store.add_to_store(printer_1, printer_2, printer_3, printer_4, printer_5, scanner_1, copier_1, copier_2, copier_3)
units = [
    "Бухгалтерия",
    "Отдел методологии",
    "Отдел контроля качества"
]
print(store.get_all_equipment())
store.add_to_unit(units[0], (printer_1, 3), (printer_3, 5), (scanner_1, 2), (copier_1, 6), (copier_1, 50))
print(store.get_all_equipment())
# Реализация (и проверка) контроля пользовательских вводов
store2 = OfficeEquipmentStore()
while True:
    user_choice = input(
        "Выберите тип орг. техники для добавления: \n 0 - Принтер\n 1 - Сканер\n 2 - Ксерокс\n Введите 'stop', чтобы остановить ввод")
    if not user_choice.lower() == "stop":
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Неверное значение данных!")
            continue
        try:
            if not user_choice:
                model, number, type = input(
                    "Введите модель (строка), количество (число), тип (строка) принтера через запятую: ").split(", ")
                store2.add_to_store(Printer(int(number), model, type))
            elif user_choice == 1:
                model, number, scan_resolution = input(
                    "Введите модель (строка), количество (число), разрешение (строка) принтера через запятую: ").split(
                    ", ")
                store2.add_to_store(Scanner(int(number), model, scan_resolution))
            elif user_choice == 2:
                model, number, copy_color_depth = input(
                    "Введите модель (строка), количество (число), скорость копирования (число) принтера через запятую: ").split(
                    ", ")
                store2.add_to_store(Copier(int(number), model, int(copy_color_depth)))
            else:
                print("Неверное значение введено! Не 0, 1, 2")
                break
        except ValueError:
            print("Введено неверное значение! ")
        except ValidationError as err:
            print(err)
            continue
    else:
        print(store2.get_all_equipment())
        break
