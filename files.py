'''
Description:
Author: Biytes
Date: 2021-04-12 20:53:34
LastEditors: Biytes
LastEditTime: 2021-04-13 11:59:51
FilePath: \python\basic\files.py
'''
# Python has functions for creating, reading, updating, and deleting files.

fileName = 'myFile.txt'

# Open a file
myFile = open(fileName, 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)
print('detail: ', myFile)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open(fileName, 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open(fileName, 'r+')
content = myFile.read(100)
print(content)