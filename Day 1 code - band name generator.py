
def gen_band_name():
    print('Welcome to the Band Name Generator.')
    # Ask about the city the user grew up in - store the input as a variable
    city = input("What's the name of the city you grew up in? \n")
    # Ask about their pet's name - store the input as a variable
    pet = input("What's your pet's name? \n")
    print("Your band name could be", city, pet + "\n")

gen_band_name()