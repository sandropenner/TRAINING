import random

class Dog:
    info = 'a fluffy boi'

    def __init__(self, name):
        print("I'm Alive!")
        self.lucky_num = random.randint(1,10)
        self.name = name
    
    def bark(self):
        print(f'My name is {self.name} and my lucky number is {self.lucky_num}')

dog1 = Dog('Max')
dog2 = Dog('Fido')

dog1.bark()
dog2.bark()

class Triangle:
    sides = 3

    def __init__(self):
        self.length = 0

    def area(self):
        return self.length * self.length
    
shape = Triangle()
shape.length = 7

print(shape.area())
