# 1
from time import sleep
# вызываем модуль для задержки
class TrafficLight: # атрибут приватный
    __color = ['красный', 'желтый', 'зеленый']

    def running(self): # метод класса
        i = 0
        while i < 3:
            print(f'Светофор переключается на : {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


TrafficLight = TrafficLight() # создали экземпляр
TrafficLight.running() # вызвали метод класса