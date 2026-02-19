# Basic class

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


user1 = User("Jeelance", 21)
user1.introduce()


# Class with multiple methods

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print(calc.add(10, 20))
print(calc.multiply(10, 20))


# Inheritance

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()


# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())


# Class method and static method

class User:
    users = 0

    def __init__(self, name):
        self.name = name
        User.users += 1

    @classmethod
    def total_users(cls):
        return cls.users

    @staticmethod
    def greet():
        return "Welcome to the application"


user1 = User("Jeelance")
user2 = User("Rahul")

print(User.total_users())
print(User.greet())