'''
Description:
Author: Biytes
Date: 2021-04-12 14:18:50
LastEditors: Biytes
LastEditTime: 2021-04-12 14:29:50
FilePath: \python\basic\lists.py
'''

fruits = list(('Mangos', 'Apple', 'Grapes', 'Oranges', 'Pears'))

# Append from list
# fruits.append('Pineapple')

# Remove from list
# fruits.remove('Pineapple')

# Insert into position

fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()
fruits.sort(reverse=True)

# Sort list
fruits.sort()

print(fruits)