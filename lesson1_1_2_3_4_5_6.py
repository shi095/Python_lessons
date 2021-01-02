# Задание 1

a = 2020
b = 1.1
c = 'Привет. Рада знакомству.'
d = 'Определим тип переменных: '

print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))

n= input('Введите любое число: ')
m= input('Введите еще одно число: ')
t= input('Напишите любой фрукт: ')


result = f'Мы задали новые переменны: n= {n}, m={m}, t={t}.'

# Задание 2

s = input('Введите любое количество секунд: ')
print('Переведем введенное вами время в формат чч:мм:сс.')
answer = int(s)
h = answer //3600
m = (answer - h * 3600) // 60
s1 = answer - h * 3600 - m * 60
print(f'Time: {h:02}:{m:02}:{s1:02}')

# Задание 3

n = input('Введите любое число n: ')
n1 = int(n)
n2 = int(f'{n}{n}')
n3 = int(f'{n}{n}{n}')
result = n1+n2+n3
print('Находим сумму чисел n + nn + nnn:')
print(f'{n1} + {n2} + {n3} = {result}')

# Задание 4

num = int(input('Введите целое положительное число: '))
max = num % 10
while num > 0:
    last = num % 10  # берем последнюю цифру
    print(last)
    num = num // 10    # убираем последнюю цифру
    if last > max:
        max = num % 10
    elif num > 9:
        continue
    else:
        print(f'Максимальное цифра в числе {max}')
        break


# Задание 5

proceeds = int(input('Введите значение выручки: ')) # значение выручки
сosts = int(input('Введите значение издержек: ')) # значение издержек
profit = proceeds - сosts # прибыль
profitability = round(profit/proceeds,2) #рентабельность
if proceeds > сosts:
    print(f'Ваша фирма прибыльна. Рентабельность выручки составляет {profitability}')
    num_empl = int(input('Введите численность сотрудников фирмы: '))
    profit_empl = round(profit / num_empl, 2)
    print(f'Прибыль фирмы в расчете на одного сотрудника {profit_empl}.')
elif proceeds == сosts:
    print(f'Ваша фирма тратит всю выручку на покрытие издержек.')
elif proceeds == 0 and сosts == 0:
    print('Ваша фирма не начала работать.')
else:
    print('Ваша фирма убыточна.')

# Задание 6

a = int(input('Сколько вы сегодня пробежали км: '))
b = int(input('Сколько максимально км вы хотели бы пробежать: '))
i = 0
print('Результат:')
while True:
    a = round(a + (0.1 * a),2)
    i = i + 1
    print(f'{i}-й день:{a}')
    if a > b:
        break
print(f'Ответ: на {i}-й день спортсмен достиг результата - не менее {b} км.')

