# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = Student("Amarjeet", 19)
# s2 = Student("Rahul", 20)

# s1.display()
# # print()
# s2.display() 




# class Car:
#      def __init__(self , brand , model):
#         self.brand=brand
#         self.model=model 
#      def car_detail(self):
#             print( "brand:" ,self.brand )
#             print("model:",self.model)
# s1=Car( "tesla","XLA")
# s2=Car( "tata", "A-12")

# s1. car_detail()
# s2.car_detail()

# Create a class BankAccount.

# Requirements:

# Account holder name
# Balance

# Methods:

# deposit(amount)
# withdraw(amount)
# check_balance()

# Rules:

# Cannot withdraw more than available balance. 

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Balance")

#     def check_balance(self):
#         print("Balance:", self.balance)

# acc = BankAccount("Amarjeet", 5000)

# acc.deposit(200000000000000000000000)
# acc.withdraw(1000000)
# acc.check_balance() 


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Balance")

#     def check_balance(self):
#         print("Balance:", self.balance)

# acc = BankAccount("Amarjeet", 5000)

# acc.deposit(2000)
# acc.withdraw(10)
# acc.check_balance()

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def inc_salary(self,percent):
#          self. salary+= self.salary*percent /100 
# emp = Employee("amarjeet" , 300000)
# emp.inc_salary( 10)
# print(emp. salary)
# # class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def increase_salary(self, percent):
#         self.salary += self.salary * percent / 100

# emp = Employee("Amarjeet", 30000)

# emp.increase_salary(10)

# print(emp.salary)




# class Animals:
#     def __init__(self, animal,  sound):
#         self.animal= animal 
#         self.sound = sound
        
#     def sound(self):
#         print(self.animal,"says:",self.sound)
        
# class Pet(Animals):
#     self.pet= ""
# s1=Animals("cat", "meow")
# s2=Animals("lion","roar")
# s1.sound()
# s2.sound()  





# class Person:
#     def __init__(self, name):
#         self.name = name

# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

# class MathTeacher(Teacher):
#     def __init__(self, name, subject, experience):
#         super().__init__(name, subject)
#         self.experience = experience

#     def display(self):
#         print("Name:", self.name)
#         print("Subject:", self.subject)
#         print("Experience:", self.experience)

# m = MathTeacher("Amit", "Math", 8)

# m.display()  


# class Person:
#     def __init__( self , name):
#         self.name=name
        
# class Teacher(Person):
#     def __init__( self, name, subject):
#         self. subject = subject
#         super().__init__(name)
# class MathTeacher(Teacher):
    
#     def __init__( self, name,subject,experience):
#         self.experience = experience
#         super().__init__(name,subject)
#     def  display(self):
#         print(" Name:",self.name)
#         print("subject:",self.subject)
#         print("experience",self.experience )
        
# m= MathTeacher( "rishi","math",2)
# m.display()   



# class Vehicle:
#     def start(self):
#         print("Vehicle Started")

# class Bike(Vehicle):
#     def start(self):
#         return("Bike Started")

# b = Bike()
# b.start()  


# class Student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

# s = Student()

# s.set_marks(90)

# print(s.get_marks())   




# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.available = True

#     def issue_book(self):
#         if self.available:
#             self.available = False
#             print("Book Issued")
#         else:
#             print("Book not available")

#     def return_book(self):
#         self.available = True
#         print("Book Returned")

# b = Book("Python", "Guido")

# b.issue_book()
# b.issue_book()
# b.return_book()
# b.issue_book()  





