class dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Nice to meet you dog')

    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old and my weight is ', self.add_weight)

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.add_weight = weight



denny = dog('denny', 23)
denny.speak()
denny.change_age(24)
denny.add_weight('7 kg')
denny.speak()

print(denny.age)



