'''
Description:
Author: Biytes
Date: 2021-04-12 17:55:57
LastEditors: Biytes
LastEditTime: 2021-04-12 18:50:23
FilePath: \python\basic\loops.py
'''

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
# for person in people:
#     print(f'Current Person: {person}')


# Break
# for person in people:
#     if person == 'Sara':
#         break
#     print(f'Current Person: {person}')

# range
# for i in range(1, 11):
#     print(f'Number: {i}')

# while loops execute a set of statements as long as a condition is true

count = 0
while count < 10:
    print(f'Count: {count}')
    count += 1

print(f'Count: {count}')
