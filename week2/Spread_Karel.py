
def main():
    
    move()
    spread()
    #
    #
    #

    pass
def spread():
    pick_beeper()
    if beepers_present():
        while beepers_present():
            move()
            if no_beepers_present():
                put_beeper()
                turn_180_degrees()
                while front_is_clear():
                    move()
                if front_is_blocked():
                    turn_180_degrees()
                    move()
                    spread()
    else:
        put_beeper()
        turn_180_degrees()
        move()
        turn_180_degrees()
                    

def turn_180_degrees():
    turn_left()
    turn_left()
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
