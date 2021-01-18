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