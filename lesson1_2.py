# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

s = input('Введите любое количество секунд: ')
print('Переведем введенное вами время в формат чч:мм:сс.')
answer = int(s)
h = answer //3600
m = (answer - h * 3600) // 60
s1 = answer - h * 3600 - m * 60
print(f'Time: {h:02}:{m:02}:{s1:02}')