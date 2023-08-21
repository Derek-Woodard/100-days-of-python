# Code on website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#See following for code to solve maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
looping = 0
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
        looping = 0
    elif not wall_on_right() and looping < 4:
        turn_right()
        move()
        looping += 1
    elif wall_in_front() and wall_on_right():
        turn_left()