class dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)


    @classmethod                       #decorators
    def num_dogs(cls):                 # cls = name of the class
        return len(cls.dogs)

    @staticmethod                      #decorators
    def bark(n):
        """bark n times"""

        for _ in range(n):
            print("Bark ! ")
# class method
denny = dog('denny')       # can call on the instance
print(denny.num_dogs())

print(dog.num_dogs())      # can call on the main class

#tim = dog("denny")

#print(tim.dogs)

# static method = they don't need class to be called
dog.bark(5)