"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import os
import json
result = []
with open(os.path.join(os.getcwd(),"text_77.json"), "w", encoding="utf-8") as my_json:
    with open(os.path.join(os.getcwd(), "text_7.txt"), encoding="utf-8") as my_file:
        profit = {}
        for line in my_file:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({"average_profit": round(average_profit)})
    json.dump(result, my_json)
