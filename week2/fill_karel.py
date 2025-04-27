from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while front_is_clear():
        sequence()
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    pass
def sequence():
    fill_row()
    check_another_row()

def fill_row():
    put_beeper()
    while front_is_clear():
        move()
        if no_beepers_present():
            put_beeper()

def check_another_row():
    turn_180_degrees()
    check_front()
    if front_is_blocked():
        if right_is_clear():
            turn_right()
            move()
            turn_right()
        if right_is_blocked():
            turn_180_degrees()
            check_front()
                

            

def check_front():
    while front_is_clear():
        move()


            
        
def turn_180_degrees():  
    turn_left()
    turn_left()

def turn_right():  
    turn_left()
    turn_left()
    turn_left()
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
