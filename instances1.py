import random

class Dog:
    info = 'a fluffy boi'

    def __init__(self, name):
        print("I'm Alive!")
        self.lucky_num = random.randint(1,10)
        self.name = name

class Office:
    volume = "it's quiet"

area = Office()
area.sound = 0

dog1 = Dog('Max')
dog2 = Dog('Fido')


print(dog1.name)
