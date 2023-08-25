# dictionares and nesting focus
# dictionaries contain a key, which is like the word in a real dictionary and an associated value, which is like the definition of the word
# a dictionary works as following: {Key: Value, Key: Value, etc...}
# Dictionaries can be oraganized with the { on the first line, then each entry on a new indented line ending with a comma, then the final } on the final line at the same indentation as the starting line
# To get something out of a dictionary: Dictionary_name[key] - will give the value of that key
# to add something to a dictionary through code: Dictionary_name["new key name"] = "definition of new key"
# Helpful to start code with an empty dictionary: empty_dictionary = {}
# Wipe an existing dictionary the same way as making a new one: old_dictionary = {}
# can edit an item in a dictionary: old_dictionary["key already in dictionary"] = "new definition"

# looping through a dictionary: can use a for loop, for i in dictionary - i will be the key, not the definition
# can use for loop to get definition by using dictionary[i] in loop

from secret_auction_art import logo

print(logo)

# Create an emptry dictionary to fill with all bidders
bidders = {}

# set a condition for the loop
more_bidders = True

while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    # Clear the screen
    

    # If there are no more bidders, finish the loop to determine the highest bidder
    if more == 'no':
        more_bidders = False

highest_bid = 0
for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of {highest_bid}.")