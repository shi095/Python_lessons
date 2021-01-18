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