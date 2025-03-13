'''# For loop - Hurdle 1
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


counter = 0

for counter in range(0, 6):
    jump()'''


# while loops:

# while something_is_true:
    #do this
    #the do this
    #then do this

'''number_of_hurdles = 6
while at_goal() == False:
    jump()
    number_of_hurdles -= 1'''
