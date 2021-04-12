'''
Description:
Author: Biytes
Date: 2021-04-12 15:10:26
LastEditors: Biytes
LastEditTime: 2021-04-12 17:54:59
FilePath: \python\basic\conditionals.py
'''




print('---------- IF/ELSE -------------')
#  IF ELSE

x = 10
y = 10

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal than {y}')
else:
    print(f'{y} is greater than {x}')


# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# not

 if not(x == y):
    print(f'{x} is not equal to {y}')


print('---------- IN -------------')

numbers = [1, 2, 3, 4, 5]
x = 4

# in
if x in numbers:
    print(x in numbers)


if x not in numbers:
    print(x not in numbers)

# is

if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)