# Code on website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#See following for code to solve maze


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
looping = 0
while not at_goal():
    if right_is_clear() and looping < 4:
        turn_right()
        move()
        looping += 1
    elif front_is_clear():
        move()
        looping = 0
    else:
        turn_left()