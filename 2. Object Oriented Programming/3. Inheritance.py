"""
class dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hi I am ', self.name, 'and I am ',self.age, 'years old')

    def talk(self):
        print('bark')

class cat(dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        self.name = 'jimmy'   # initialize the upper speak method and change it here.

    def talk(self):
        print('meow')

jim = dog('jim', 23)
jim.talk()


denny = cat('denny', 7, 'red')
denny.speak()
denny.talk()
"""


class veichle(object):
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fill_up_tank(self):
        self.gas = 100

    def empty_tank(self):
        self.gas = 0

    def gas_left(self):
        return self.gas

class Car(veichle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print("beep beep")

class truck(veichle):
    def __init__(self, price, gas, color, tires,):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print('honk honk')




