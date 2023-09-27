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
this opens the file in read-only mode

to write to a file, start the same way, but open it :
with open('file path', mode="w") as file:
    file.write('new text.')
this deletes the previous file
to add the text, use mode="a" to append instead

ex:
with open('file path', mode="a") as file:
    file.write('\nnew text.')

opening a file in write mode will create a new file from scratch
'''

# os.chdir('Day 24 - Mail Merge\Improved Snake Game')
with open('Day 24 - Mail Merge/Improved Snake Game/test.txt') as file:
    contents = file.read()
    print(contents)

with open('Day 24 - Mail Merge/Improved Snake Game/test.txt', mode="a") as file:
    file.write('\nnew text.')
    print(contents)
