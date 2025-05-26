from karel.stanfordkarel import *

def main():
    while front_is_clear():
        create_wave()
   
def create_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    spin_180()
    move()
    turn_left()
    if(front_is_clear()):
        move()
        move()

def turn_right():
    for i in range(3):
        turn_left()

def spin_180():
    for i in range(2):
        turn_left()


if __name__ == '__main__':
    main()
