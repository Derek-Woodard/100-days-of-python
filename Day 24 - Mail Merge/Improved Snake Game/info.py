'''
You can use Python to read/write files on your computer
can use open('text file name.txt') and set it as a variable
you can then use a new variable to read() the file to get the string
ex.
file = open('info.txt')
contents = file.read()
print(contents)
'''
import os
import sys

file = open(os.path.join(sys.path[0], "info.txt"), "r")
# file = open('info.txt')
contents = file.read()
print(contents)
