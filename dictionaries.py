'''
Description:
Author: Biytes
Date: 2021-04-12 14:45:55
LastEditors: Biytes
LastEditTime: 2021-04-12 14:55:59
FilePath: \python\basic\dictionaries.py
'''

# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members

# Create Dictionary

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, person['first_name'], type(person))

# Use constructor
# person = dict(first_name='Sara', last_name='Williams')

print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-5555'

# print(person.keys())

# print(person.values())

# print(person.items())

# Copy dict

person2 = person.copy() # 深拷贝

person2['city'] = 'ShenZhen'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
# person.clear()

# length
print(f'length is {len(person)}')

print(person)