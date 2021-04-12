# A class is like a blueprint for creating objects. An object has properties and methods
# (functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'


    def has_birthday(self):
        self.age += 1

# Extend class [User passed as a parameter]
    # Constructor
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance




# Init user object

brad = User('Brad Traversy', 'brad@gmail.com', 37)

brad.set_balance(100)

print(brad.name, type(brad), brad.balance)
print(brad.has_birthday())

print(brad.greeting())

