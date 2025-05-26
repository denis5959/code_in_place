# Write a console program which asks the user
# for their height in meters and prints whether
# or not they are the correct height to be a NASA astronaut.

def main():
    user_weight = float(input("Enter your height in meters: ")) #First, we ask the user for their height, using the console
    if(user_weight<= 1.6): #After receiving the value, we evaluate it to determine where it belongs
        print("Below minimum astronaut height")
    elif(user_weight> 1.6 and user_weight < 1.9): #We use an "and" operator to compare two different variables
        print("Correct height to be an astronaut")
    else: #There is no need to compare the last case since it is the only option available left
        print("Above maximum astronaut height")
pass

if __name__ == "__main__":
    main()
