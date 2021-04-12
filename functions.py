'''
Description:
Author: Biytes
Date: 2021-04-12 15:00:17
LastEditors: Biytes
LastEditTime: 2021-04-12 15:08:59
FilePath: \python\basic\functions.py
'''

# A function is a block of code which only runs when it is called. In python, we do not use curly brackets, we use indentation with tabs or spaces


print('---------- Basic -------------')
# Create fcuntion
def sayHello(name='Sam'):
    print(f'Hello {name}')


sayHello('John Doe')

sayHello()

# Return Values
def getSum(num1, num2):
    total = num1 + num2
    return total

print('abc ' + str(getSum(1,2)))
print('---------- lambda -------------')

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one experssion. Very similar to JS arrow functions.

getSum = lambda num1, num2 : num1 + num2

print(getSum(10,3))