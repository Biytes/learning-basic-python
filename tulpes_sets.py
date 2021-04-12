'''
Description:
Author: Biytes
Date: 2021-04-12 14:30:03
LastEditors: Biytes
LastEditTime: 2021-04-12 14:45:45
FilePath: \python\basic\tulpes_sets.py
'''

# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members

# Create tuple

fruits = ('Apples', 'Oranges', 'Grapes')


print(fruits[1], type(fruits), len(fruits))

# fruits = tuple(('Apples', 'Oranges', 'Grapes'))

# Delete tuple
# del fruits


# A Set is a collection which is unordered and unindexed. No dulipicate members

fruits_set = {'Apples', 'Oranges', 'Grapes'}


# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# clear set
fruits_set.clear()

del fruits_set

print(fruits_set)
