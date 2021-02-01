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

# 4

class Car:

    def __init__(self,speed,color,name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина марки {self.name} поехала.'

    def stop(self):
        return f'Машина марки {self.name}  остановилась.'

    def turn_left(self):
        return f'Машина марки {self.name} повернула налево'

    def turn_right(self):
        return f'Машина марки {self.name}  повернула направо.'

    def show_speed(self):
        return f'Скорость машины марки {self.name} составлет {self.speed}.'

class TownCar(Car):
    def __init__(self,speed,color,name, is_police):
        super().__init__(speed,color,name, is_police)

    def show_speed(self):
        print(f'Скорость машины марки {self.name} составлет {self.speed}.')
        max_speed = 60
        if self.speed > max_speed:
            return f'Скорость машины марки {self.name} выше {max_speed}. Сбавьте скорость'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self,speed,color,name, is_police):
        super().__init__(speed,color,name, is_police)

    def show_speed(self):
        print(f'Скорость машины марки {self.name} составлет {self.speed}.')
        max_speed = 40
        if self.speed > max_speed:
            return f'Скорость машины марки {self.name} выше {max_speed}. Сбавьте скорость'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == True:
            return f'Машина марки {self.name} - полицейская машина.'
        else:return f'Машина марки {self.name} - не полицейская машина.'



KIA = TownCar(70,'желтый','KIA', False)
AUDI = SportCar(150,'черный','AUDI', False)
WV = WorkCar(50,'красный','WV', False)
FORD = PoliceCar(100,'синий','FORD', True)

print(KIA.go())
print(KIA.stop())
print(KIA.turn_left())
print(KIA.turn_right())
print(KIA.show_speed())


print(AUDI.go())
print(AUDI.stop())
print(AUDI.turn_left())
print(AUDI.turn_right())
print(AUDI.show_speed())

print(WV.go())
print(WV.stop())
print(WV.turn_left())
print(WV.turn_right())
print(WV.show_speed())


print(FORD.go())
print(FORD.stop())
print(FORD.turn_left())
print(FORD.turn_right())
print(FORD.show_speed())
print(FORD.police())