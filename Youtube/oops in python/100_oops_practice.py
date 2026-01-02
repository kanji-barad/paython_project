# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(f"student name is {self.name} and age is {self.age}")

# s1=Student('kanji',23)
# s1.display()

# class Employe:
#     company='TCS'
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def info(self):
#         print(f"employee company is {Employe.company} and employe name is {self.name} and current salary is {self.salary}")

# s1=Employe('kanji',50_000)
# s1.info()


"""
BankAccount class બનાવો જેમાં:

private variable __balance

methods:

deposit(amount)

withdraw(amount)

show_balance()
"""

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance

#     def deposite(self,amount):
#         self.__balance+=amount
#         print("deposite succesfully")
    
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             print('withdrawal succesfully')
#         else:
#             print('not enghouh balance')
    
#     def show_balance(self):
#         print(self.__balance)
    
# b1=BankAccount(50_000)
# b1.deposite(20_000)
# b1.withdraw(50_000)
# b1.show_balance()

"""
Person class બનાવો:

private variable __age

setter: set_age()

getter: get_age()

age positive હોવી જોઈએ
"""

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
    
#     def set_age(self,new):
#         self.new=new
#         if self.__age<0:
#             self.__age=self.new
#         else:
#             print('negative age is not valid')

        
#     def get_age(self):
#         return self.__age
    
# p1=Person('kanji',22)
# p1.set_age(-23)
# print(p1.get_age())



"""
Vehicle class → method start()

Bike class → Vehicle થી inherit કરે

Bike object થી start() call કરો
"""

# class Vehical:
#     def start(self):
#         print("vehical is starting")

# class Bike(Vehical):
#     pass

# b1=Bike()
# b1.start()


"""
Animal class → method sound()

Dog class → sound() override કરે
"""

# class Animal:
#     def sound(self):
#         print('animal class')

# class Dog(Animal):
#     def sound(self):
#         print('dog class')

# d1=Dog()
# d1.sound()

# a1=Animal()
# a1.sound()


"""
Father class → method skills()

Mother class → method skills()

Child class → બંને inherit કરે
"""

# class Father:
#     def skill(self):
#         print('farmer')

# class Mother:
#     def skill(self):
#         print('housewife')

# class Child(Father,Mother):
#     #~ jyare hu father ane mother banne ni skills inherit kari ane skill n call karu tyare left to right (MRO) follow kare che 
#     #~ Both Parent Skills Access કરવા (Override + super) aa banne access kri sakiye chiye.
#     def skill(self):
#         Father.skill(self)
#         Mother.skill(self)
#         print('child is learning')

# c1=Child()
# c1.skill()
    
"""
એક loop માં અલગ-અલગ class ના objects પર એકજ method call કરો.

Example:

Car, Bike, Bus

method: fuel_type()
"""

# class Bike:
#     def fuel_type(self):
#         print("bike uses petrol")

# class Car:
#     def fuel_type(self):
#         print('car usese petro and disel')

# class Bus:
#     def fuel_type(self):
#         print('bus is usese gas')

# vehical=[Bike(),Car(),Bus()]

# for v in vehical:
#     v.fuel_type()

"""
College class બનાવો:

class method → college name

static method → simple message print કરે
"""

# class College:
#     colleage_name='parul university'

#     def college_greet(self):
#         print(College.colleage_name)

#     @staticmethod
#     def welcome_message():
#         print("welcome to our college")

# c1=College()
# c1.college_greet()
# c1.welcome_message()


