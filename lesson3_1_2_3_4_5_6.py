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
