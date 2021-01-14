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

# 5

from functools import reduce #используем модуль

def reducer_func(el_prev, el): #перемножаем элементы с помощью функции
    return el_prev*el

l=[el for el in range(100,1000) if el % 2 == 0] #используем  генератор списка

print(l) #лист с четными числами от 100 до 1000

print(reduce(reducer_func,l)) #произведение всех элементов списка

# 6.а
def generator():            #объявляем функцию для создания генератора
    for el in range(3, 10):
        yield el            # yield возвращает нам не значение, а генератор

g = generator()
for el in g:
    print(el)

# 6.б

from itertools import count #функция count из модуля
for i in count(10):         # начинаем генерировать числа с 10 в этом нам помогает функция count
    if i > 20:
        break               #как только мы достигаем 20го числа выходим из цикла
    else:
        print(i)            #печатаем целые числа


from itertools import cycle #функция cycle из модуля
list = [1,2,3,4]            #объявляем список
count=1
for el in cycle(list):      # начинаем повторять элементы из списка
    if count > 20:          # ставим ограничение, что повторений не больше 20 раз
        break
    print(el)
    count += 1