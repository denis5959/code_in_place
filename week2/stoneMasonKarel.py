from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    sequence()
    sequence()
    last_sequence()
    
    pass
def sequence():
    build_column()
    ascend()
    descend()
    prepare_column()

def last_sequence():
    build_column()
    ascend()
    turn_right()
    escalation_movement()
    escalation_movement()
    turn_right()
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
        if front_is_blocked():
            turn_left() 

def build_column():
    turn_left()
    put_beeper()
    while front_is_clear():
        for i in range(4):
            move()
            put_beeper()

def ascend():
    if front_is_blocked():
        while right_is_clear():
            escalation_movement()
            
def escalation_movement():
    turn_right()
    move()
    turn_left()
    move()

def descend():
    turn_right()
    while front_is_blocked():
        if right_is_clear():
            escalation_movement()



def prepare_column():
    turn_right()
    if front_is_clear():
        while right_is_clear():
            move()
            if front_is_blocked():
                turn_left()

def turn_right():
    for i in range(3):
        turn_left()
if __name__ == '__main__':
    main()
