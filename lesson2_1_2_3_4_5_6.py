# 1.

l = ['Да', 1, 34.5, None]
print(l)

for elem in l:
    elem = type(elem)
    print(elem)

# 2
answer = list(input('Заполните любыми значениями список: '))
print(answer)
# Обмениваем значениями элементы с индексами 0 и 1, 2 и 3 и т.д.
for elem in range(0,len(answer),2):
        answer[elem],answer[elem+1] = answer[elem+1],answer[elem]
        answer.append(answer[-1])

print(answer)
#застряла на том, что если неченое потом выводит несколько раз.
# понимаю, что проблема в цикле, но как решить - не понимаю.

# 3

dict = {"1":"январь- это зима",
     "2":"февраль - это зима",
     "3":"март - это весна",
     "4":"апрель - это весна",
     "5":"май - это весна",
     "6":"июнь - это лето",
     "7":"июль - это лето",
     "8":"август - это лето",
     "9":"сентябрь - это осень",
     "10":"октябрь - это осень",
     "11":"ноябрь - это осень",
     "12":"декабрь - это зима"}
answer = input('Введите месяц года в виде целого числа от 1 до 12: ')
print(f'Вы ввели {answer} месяц года: {dict[answer]}.')

# 4

answer = input('Введите любое количество слов через пробел: ')
for i, answer in enumerate(answer.split()):
    print(i+1, "\n".join(answer[:10].split()))
    break

# 5

my_list = [7,5,3,2,2]
print(f'Рейтинг - {my_list}')
element = int(input('Введите новый элемент рейтинга. Для остановки введите 100: '))
while element !=100:
    for elem in range(len(my_list)):
        if my_list[elem] == element:
            my_list.insert(elem + 1, element)
            break
        elif my_list[elem] > element and my_list[elem + 1] < element:
            my_list.insert(elem+1, element)
        elif my_list[0] < element:
            my_list.insert(0, element)
        elif my_list[-1] > element:
            my_list.append(element)

    print(f'Новый рейтинг - {my_list}')
    element = int(input('Введите новый элемент рейтинга. Для остановки введите 100: '))

print(f'Окончательный рейтинг - {my_list}')