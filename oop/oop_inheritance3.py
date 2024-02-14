# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name, self.age)
#
# class Student(Person):
#     def __init__(self, name, age, dob):
#         self.sName = name
#         self.sAge = age
#         self.dob = dob
#
#         # inheriting the properties of parent class
#         super().__init__('Rahul', age)
#
#     def displayInfo(self):
#         print(self.sName, self.sAge, self.dob)
#
# obj = Student('Mayan', 23, '16-03-2000')
# obj.display()
# obj.displayInfo()


class Base1:
    def __init__(self):
        self.str1 = 'Geek12'
        print('Base1')


class Base2:
    def __init__(self):
        self.str2 = 'Geek21'
        print('Base2')


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print('Derived')

    def printStrs(self):
        print(self.str1, self.str2)


# ob = Derived()
# ob.printStrs()


class Base:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Child(Base):

    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address


g = GrandChild('Max', 23, 'Noida')
# print(g.getName(), g.getAge(), g.getAddress())


class C:
    def __init__(self):
        self.c = 21
        self.__d = 42

class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)


object = D()

print(object.c)
print(object.e)
# d is private so child can't call this variable
print(object.d)