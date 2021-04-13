'''
Description:
Author: Biytes
Date: 2021-04-13 12:03:22
LastEditors: Biytes
LastEditTime: 2021-04-13 14:11:50
FilePath: \python\basic\py_json.py
'''

# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dictionary
user = json.loads(userJSON)

print(user)


# reverse JSON
car = {'make': "Ford", 'model': "Mustang", 'year': 1970}
carJSON = json.dumps(car)

print(carJSON)

