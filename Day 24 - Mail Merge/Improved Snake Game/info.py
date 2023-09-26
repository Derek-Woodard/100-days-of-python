'''
You can use Python to read/write files on your computer
can use open('text file name.txt') and set it as a variable
you can then use a new variable to read() the file to get the string
ex.
file = open('info.txt')
contents = file.read()
print(contents)
file.close()

can use to avoid the need to close the file
with open('file_name.txt') as file:
    contents = file.read()
    print(contents)
'''

# os.chdir('Day 24 - Mail Merge\Improved Snake Game')
with open('Day 24 - Mail Merge/Improved Snake Game/test.txt') as file:
    contents = file.read()
    print(contents)
