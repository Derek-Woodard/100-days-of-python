#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letters_used = 0
numbers_used = 0
symbols_used = 0

password = ""
# for character in range(0, (nr_letters + nr_symbols + nr_numbers) + 1, 1):
while len(password) < (nr_letters + nr_symbols + nr_numbers):
    char_order = random.randint(1,3)
    if char_order == 1 and letters_used < nr_letters:
        password += random.choice(letters)
        letters_used += 1
    elif char_order == 2 and numbers_used < nr_numbers:
        password += random.choice(numbers)
        numbers_used += 1
    elif char_order == 3 and symbols_used < nr_symbols:
        password += random.choice(symbols)
        symbols_used += 1

print(f"Your password is: {password}")

# Can create easy version by simply ranomly selecting the characters of each type
# to make it the hard version, there is a function called random.shuffle() that will randomize the order of a list