
#1. Поработайте с переменными, создайте несколько, выведите на экран,
#запросите у пользователя несколько чисел и строк и
#сохраните в переменные, выведите на экран.

age=20
name="Alex"
km=2.3159
answer=True
print("Ваш возраст", age, "type:", type(age))
print("Ваше имя", name, "type:", type(name))
print("Расстояние от Вашего дома до университета", km, "type:", type(km))
print("%.2f" %km)
print("Понравилось ли Вам первое занятие", answer, "type:", type(answer))
print("It's %s, my age is %d. I live %f  km from my University" %(name, age, km))
surname = input("Введите Вашу фамилию ")
print("Ваша фамилия", surname, "type:", type(surname))
password = input("Введите Ваш пароль ")
print("Ваш пароль", password, "type:", type(password))
print("My surname is {}. My password is {}." .format(surname,password))