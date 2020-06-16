"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
 расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
 (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений
  необходимо запускать скрипт с параметрами.
"""

from sys import argv

def calculating_salary (work_hours: int, hourly_rate: float, premium: float):
    return (work_hours * hourly_rate) + premium

try:
    script_name, work_hours, hourly_rate, premium = argv
    print(f"Заработная плата сотрудника: { calculating_salary (int(work_hours), float(hourly_rate), float(premium))} руб.")
except ValueError:
    print(f"При запуске скрипта произошла ошибка! Передайте параметры с следующий раз правильно - числами.")
