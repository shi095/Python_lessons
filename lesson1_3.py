# 3. Узнайте у пользователя число n.
#    Найдите сумму чисел n + nn + nnn.
#    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите любое число n: ')
n1 = int(n)
n2 = int(f'{n}{n}')
n3 = int(f'{n}{n}{n}')
result = n1+n2+n3
print('Находим сумму чисел n + nn + nnn:')
print(f'{n1} + {n2} + {n3} = {result}')