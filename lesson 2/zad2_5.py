# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с
# тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
t_user_len = len(my_list)
user_len = len(my_list)
user_number = input(f"Введите число в рейтинг {my_list}")
# Проверка является ли введенный элемент числом
if user_number.isnumeric():
    # Преобразование в целочисленный тип данных
    user_number = int(user_number)
    # Введенное число сравниваем с каждым элементом списка. Если оно больше данного элемента, то
    # это число размещается в списке на позиции перед ним.  Если будет несколько одинаковых элементов в списке, и
    # вставляется ещё один такой же элемент, то он вставится после уже имеющихся, т.е. будет сравниваться с тем, который
    # уже стоит после повторяющихся.
    for el in my_list:
        if user_number > el:
            my_list.insert(my_list.index(el), user_number)
            user_len +=1
            break
    # Если число меньше натуральных чисел нашего набора, а значит мы его еще не вставили,
    # проверяем это с помощью построки и добавляем в конец строки
    if my_list.count(user_number) == 0:
        my_list.append(user_number)
    if user_len == t_user_len:
        my_list.append(user_number)
    print(f"Получившийся рейтинг: {my_list}")
