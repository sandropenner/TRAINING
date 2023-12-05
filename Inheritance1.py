import random

class Animal:
    info = 'a living organism'

    def __init__(self, name):
        print("animal is created")
        self.name = name

class Dog(Animal):
    info = 'fluffy bois'

    def __init__(self, name):
        super().__init__(name)
        print("It's Alive!")
        self.lucky_num = random.randint(1,10)
        self.fur = ""

    
    def bark(self):
        print(f'My name is {self.name} and my lucky number is {self.lucky_num}')

class Bulldog(Dog):
    def __init__(self, name):
        super().__init__(name)
        print('Bulldog boi here!')

dog1 = Bulldog('Max')
dog1.bark()

class Poodle(Dog):
    def __init__(self, name):
        super().__init__(name)
        print("It's a poodle!")


dog2 = Poodle('Fido')
dog2.bark()

print("We are", dog1.info)