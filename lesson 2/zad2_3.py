# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через list
# Пока условие верно -прекращается или break или print
while True:
    # Ввод месяца в виде целого числа от 1 до 12
    user_number = input("Введите число от 1 до 12")
    # Объявление списков времен года, где опредлим к какому времени года относится месяц,
    # а если точнее времени года определим соотвествующие месяцы
    winter = [1, 2, 12]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    # Проверка, что введенное значение является числом, потому как именно эта функция
    # возвращает true, если все символы в строке являются числовыми. В нашем случае возможно
    # и использование isdigit
    if user_number.isnumeric():
        # Преобразование в целочисленный тип данных
        user_number = int(user_number)
        if user_number in winter:
            print("Зима")
        elif user_number in spring:
            print("Весна")
        elif user_number in summer:
            print("Лето")
        elif user_number in autumn:
            print("Осень")
        else:
            print("Ошибка, Вы ввели неправильные данные, необходимо число от 1 до 12!")
            break
        break
    else:
        print("Ошибка, Вы ввели неправильные данные, необходимо число от 1 до 12!")

# Решение через dict
while True:
    # Ввод месяца в виде целого числа от 1 до 12
    user_number = input("Введите число от 1 до 12")
    # Объявление словаря, содержащего времена года c относящимися к ним месяцами
    seasons = {'winter': [1, 2, 12], 'spring':[3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
    if user_number.isnumeric():
        user_number = int(user_number)
        if user_number in seasons['winter']:
            print("Зима")
        elif user_number in seasons['spring']:
            print("Весна")
        elif user_number in seasons['summer']:
            print("Лето")
        elif user_number in seasons['autumn']:
            print("Осень")
        else:
            print("Ошибка, Вы ввели неправильные данные, необходимо число от 1 до 12!")
            break
        break
    else:
        print("Ошибка, Вы ввели неправильные данные, необходимо число от 1 до 12!")
