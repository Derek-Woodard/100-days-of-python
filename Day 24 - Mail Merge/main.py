'''take a list of names and insert them into a letter'''

#TODO make a list of names in a text file called invited_guests.txt
#TODO make a default letter script
#TODO Access the names to write letter to each person using script
#TODO save the letters to another folder

# use the following: readlines(), replace(), strip() for strings

with open('Day 24 - Mail Merge/Input/Letters/starting_letter.txt') as base_template:
    template = base_template.read()
    print(template)

TEMP = "\n"

with open('Day 24 - Mail Merge/Input/Names/invited_names.txt') as names:
    while TEMP:
        TEMP = names.readline()
        TEMP.strip()
        print(TEMP)
        