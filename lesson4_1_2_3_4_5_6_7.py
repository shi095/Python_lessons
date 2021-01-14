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