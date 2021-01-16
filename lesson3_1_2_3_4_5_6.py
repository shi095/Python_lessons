# Не смотрю решения Урока 3, потому что хочу сама разобраться.
# Заполняю по мере выполнения
# 1
def devision(num1,num2):
    return num1/num2
# создаем исключение, что на ноль делить нельзя
try:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    devision(num1,num2)
except ZeroDivisionError as e:
    print(e)
finally:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print(devision(num1,num2))

# 2

def person(name,surname,birthday,current_city,email,phone):
    return f'Даные пользователя: {name} {surname} {birthday} {current_city} {email} {phone}'
dict = {"name":"Иван",
"surname":"Иванов",
"birthday":"01/02/2012",
"current_city":"Москва",
"email":"s@g",
"phone":"1234"}

info = person(**dict)

print(info)
# 3

def my_func(arg1,arg2,arg3):
    if min(arg1,arg2,arg3):
        return arg2 + arg3
    elif min(arg1,arg2,arg3):
        return arg1 + arg3
    else:
        return arg1 + arg2

answer = my_func(1,2,3)

print(answer)

# 4
def my_func(x, y):
    return x ** y


arg = my_func(2, -3)

print(arg)

# на второй способ не хватило сил

# 5

my_list = list(map(int,input('Введите строку чисел через пробел. Для остановки введите 100: ').split()))

def sum_list(my_list):
    return sum(my_list)

i = 0
while 100 not in my_list:
    for i in range(len(my_list)):
        elem = my_list[i]
    print(f'Сумма введенных вами чисел равна {sum_list(my_list)}')
    i += 1
    my_list.extend(list(map(int, input('Введите строку чисел через пробел. Для остановки введите 100: ').split())))

# Честно скажу. Ковырялась долго в 5ом задании. Но алгоритм работает.

#6
text = input('Введите любой текст латинскими буквами:')

def int_func(text):
    return text.capitalize()

print(int_func(text)) #Верхний регистр только первой буквы

print(int_func(text).title()) #Верхний регистр первой буквы каждого слова

# Урок 3 полностью готов для проверки
