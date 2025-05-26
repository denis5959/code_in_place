from karel.stanfordkarel import *

def main():
    while front_is_clear():
        create_wave()
   
def create_wave():
    #This will create the base of the wave
    put_beeper()
    move()
    put_beeper()

    #This creates the high part of the tide
    turn_left()
    move()
    put_beeper()
    spin_180()
    move()

    #Goes into final position position
    turn_left()

    #If the front is clear, we create another wave, if not, we stop where we left
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
