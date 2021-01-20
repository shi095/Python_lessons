# создана ветка для выполнения заданий 1-7 Урока 5
# 1
from io import TextIOWrapper

messages = list()
message = 0
while message != "":
        message = input("Введите строку: ")
        messages.append(message + "\n")
        if message == "":break


with open("text.txt", "w") as file:
        for message in messages:
                file.write(message)

# 2

from io import TextIOWrapper, BufferedWriter

with open('text5_2.txt','r') as f: # вывожу на экран содержимое файла для пользователя
    lines = f.read()
    print(lines)

with open('text5_2.txt', 'r') as f: # создаю лист из строк
    list = f.read().splitlines()

lines = len(list)

print(f'Количество строк в файле: {lines}')

i = 0
while i < len(list):
    print(f'В строке {i+1} количество слов: {len(list[i].split())} ')
    i += 1

# 3
from io import BufferedReader, TextIOWrapper


with open('text5_3.txt','r',encoding='UTF-8') as salary:
    workers = {}
    for line in salary:
        key, value = line.split()
        workers[key] = int(value)
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
    result = sum(workers.values())/len(workers)

print(f'Средняя величина дохода сотруднкиов: {result}')

# 4

from io import BufferedReader, TextIOWrapper


with open('text5_4.txt', encoding='UTF-8') as number:
    list = number.read().split()
    dict_translate = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}

    for item in list:
        if item in dict_translate:
            list[list.index(item)] = dict_translate[item]
    new_list = [list[d:d+3] for d in range(0, len(list), 3)]

with open("text5_4_1.txt", "w",encoding='UTF-8') as number_new:
    text5_4_1 = 0
    for row in new_list:
        text5_4_1 = ' '.join(map(str, row))
        number_new.write("{}\n".format(text5_4_1))
        print(text5_4_1)

# 5

from io import BufferedReader, TextIOWrapper


with open('text5_5.txt','w') as answer_number:
    answer_number.write('1 2 3 4 5')

with open('text5_5.txt','r') as number:
    list_num = []
    for line in number:
        list_num = line.split()
    list_num  = list(map(int, list_num))

print(f'Сумма чисел в text5_5.txt: {sum(list_num)}')

# 6

from io import BufferedReader, TextIOWrapper

with open("text5_6.txt", encoding='utf-8') as lessons:
    lines = lessons.readlines()
    subjects = {}
    for line in lines:
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
    print(f'Словарь: {subjects}')