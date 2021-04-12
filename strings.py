'''
Description:
Author: Biytes
Date: 2021-04-12 11:14:45
LastEditors: Biytes
LastEditTime: 2021-04-12 14:59:42
FilePath: \python\basic\strings.py
'''
name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting


# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-String (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'

print(s.capitalize())