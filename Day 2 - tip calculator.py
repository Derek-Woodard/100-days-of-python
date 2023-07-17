def pay_tip():
    print('Welcome to the tip calculator.')
    bill = float(input('What was the total bill? '))
    num_people = int(input('How many people to split the bill? '))
    tip_percent = float(input('What percentage tip would you like to give? 10, 12, or 15? '))
    tip_amount = round((bill / num_people) * (1 + (tip_percent / 100)),2)
    rounded_tip = "{:.2f}".format(tip_amount)
    print('Each person should pay: $' + rounded_tip)

pay_tip()