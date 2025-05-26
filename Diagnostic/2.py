# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100
def main():
    for i in range(1, MAX_NUMBER + 1): # Starts at 1 and includes 100.
    # If we used just MAX_NUMBER, the loop would stop at 99
        if i%2 == 0: #Divides the number between 2, if the remainder is cero, it is even.
            print(str(i) + " is even") #In order to print it, we need to convert our "i" variable into a string
        else: #If the remainder is not 0, it is odd. Since there are only two cases again, there is no need to reevaluate the variable.
            print(str(i) + " is odd")
    pass

if __name__ == "__main__":
    main()
