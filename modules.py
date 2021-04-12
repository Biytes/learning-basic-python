'''
Description:
Author: Biytes
Date: 2021-04-12 18:50:37
LastEditors: Biytes
LastEditTime: 2021-04-12 20:31:59
FilePath: \python\basic\modules.py
'''

# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules by python
print('---------- Core -------------')

import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# import custom module
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

print(today)
print(timestamp)

print('---------- Pip Modules ----------')

c = CamelCase()

print(c.hump('hello there world'))

print(validate_email('1653082552@qq.com'))

if validate_email('1653082552@qq.com'):
    print('email is valid')
else:
    print('email is invalid')



