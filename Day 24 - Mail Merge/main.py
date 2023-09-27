'''take a list of names and insert them into a letter'''

# make a list of names in a text file called invited_guests.txt
# make a default letter script
# Access the names to write letter to each person using script
# save the letters to another folder

# use the following: readlines(), replace(), strip() for strings

with open('Day 24 - Mail Merge/Input/Letters/starting_letter.txt') as base_template:
    template = base_template.read()

with open('Day 24 - Mail Merge/Input/Names/invited_names.txt') as names:
    name_list = names.readlines()

for name in name_list:

    stripped_name = name.strip()

    new_letter = template.replace("[name]", stripped_name)
    letter_name = f"Letter_for_{stripped_name}.txt"

    with open(f"Day 24 - Mail Merge/Output/ReadyToSend/{letter_name}", "w") as output_letter:
        output_letter.write(new_letter)
