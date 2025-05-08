import random

def main():
    sides = input("How many sides does your dice have? ")
    amount = random.randint(1, int(sides))
    print("Your roll is " + str(amount))




if __name__ == '__main__':
    main()
