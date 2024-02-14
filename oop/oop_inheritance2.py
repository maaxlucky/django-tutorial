# class Person(object):
#
#     # Constructor
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     # To check if this person is an employee
#     def display(self):
#         print(self.name, self.id)
#
#
# # Driver code
# emp = Person('Saitama', 102)
# # emp.display()
#
#
# class Emp(Person):
#
#     def Print(self):
#         print('Emp class called')
#
# Emp_details = Emp('Mayank', 103)

# Emp_details.display()
# Emp_details.Print()

# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def isEmployee(self):
#         return False
#
#
# class Employee(Person):
#     def isEmployee(self):
#         return True
#
#
# emp = Person('Greek')
# print(emp.getName(), emp.isEmployee())
#
# emp = Employee('Greek2')
# print(emp.getName(), emp.isEmployee())

class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)


a = Employee('Rahul', 104, 20000, 'Intern')


# a.display()

class A:
    def __init__(self, name='Rahul'):
        self.name = name


class B(A):
    def __init__(self, roll):
        self.roll = roll

        # A.__init__(self)


object = B(23)
# we will get error because we did not init name in B class
print(object.name)
