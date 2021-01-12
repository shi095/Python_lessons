# Не смотрю решения Урока 3, потому что хочу сама разобраться.
# Заполняю по мере выполнения
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

# Честно скажу. Ковырялась долго в этом задании. Но алгоритм работает.