# Cоздана ветка для наполнения заданиями к уроку 4
# 1
# Через командную строку переходим в папку, в которой хранится скрипт
# C:/Users/shilo/PycharmProjects/pythonProject_2020/venv/
# формируем лист для расчета заработной платы сотрудника
# python lesson4_1.py 8 20 200
# ['lesson4_1.py', '8', '20', '200'] - лист
# 360  - полученный результат

from sys import argv
print(argv)

def salary_func(sal_hour,hour,bonus):
    return int(sal_hour)*int(hour)+int(hour)

print(salary_func(argv[1],argv[2],argv[3]))

#2
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_new = [el for num,el in enumerate(list) if list[num-1]<list[num]]
print(list_new)

#3

l = [el for el in range(20,241) if el % 20 == 0 or el % 21 == 0]
print(l)

#4

#вариант 1 с использованием модуля и генератора

from collections import Counter

l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(list([k for k, v in Counter(l).items() if v == 1]))
#вариант 2 с использованием генератора. Но не могу додумать как тут оставить элемент в исходном порядке

print(list(set([i for i in l if l.count(i) < 2])))