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

# 2

class Road:

    def __init__(self,length,width):
        self._length = length
        self._width = width


    def mass_of_asphalt(self, mass,thickness):
        return self._length*self._width*mass*thickness

r = Road(20,5000)
result =r.mass_of_asphalt(25,5)
print(f'Масса асфальта,необходимого для покрытия всего дорожного полотна:{result}кг.')