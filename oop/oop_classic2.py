# class Dog:
#
#     # attributes
#     attr1 = 'mammal'
#     attr2 = 'dog'
#
#     def fun(self):
#         print('I am a', self.attr1)
#         print('I am a', self.attr2)
#

# Rodger = Dog()

# print(Rodger.attr1)
# Rodger.fun()

class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def __str__(self):
        return f'My name is {self.name} and I work in {self.company}'

    def show(self):
        print(f'Hello my is {self.name} and I work in {self.company}')


obj = GFG('John', 'GeekForGeeks')
# obj.show()
# print(obj)


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'Hello my name is {self.name}')


p = Person('Nikhil')
# p.say_hi()

class Cat:
    animal = 'cat'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


Vaska = Cat('Domestic', 'White')
Bobo = Cat('British', 'Black')

# print('Vaska details:')
# print('Vaska is a', Vaska.animal)
# print('Breed: ', Vaska.breed)
# print('Color: ', Vaska.color)
#
# print('\nBobo details:')
# print('Bobo is a', Bobo.animal)
# print('Breed: ', Bobo.breed)
# print('Color: ', Bobo.color)
#
# # class variables can be accessed using class
# print('\nAccessing class variable using class name')
# print(Cat.animal)

class Dog:
    animal = 'dog'

    def __init__(self, breed):
        self.breed = breed

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color


Rodger = Dog('Pug')
Rodger.setColor('brown')
print(Rodger.getColor())