'''
Description:
Author: Biytes
Date: 2021-04-12 19:54:58
LastEditors: Biytes
LastEditTime: 2021-04-12 19:59:37
FilePath: \python\basic\validator.py
'''

import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a=zA=Z0-9-.]+.([a-zA-Z]{2, 3}|[0-9]{1,3})(]?)$", email))