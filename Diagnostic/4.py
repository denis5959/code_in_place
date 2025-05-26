def main():
    #We ask the user to begin entering numbers
    print("Enter a sequence of non-decreasing numbers.")
    
    #Get the first number in the sequence
    previous_number = float(input("Enter num: "))
    
    #Start the sequence length at 1 (since we already got the first number)
    sequence = 1

    #Keep asking for numbers until the user breaks the non-decreasing rule
    while True:
        #Ask the user for the next number in the sequence
        secondary_number = float(input("Enter num: "))

        # We evaluate if the new number is greater than or equal to the previous one in the sequence
        if secondary_number >= previous_number:
            sequence += 1  # Increase sequence count
            previous_number = secondary_number  # Update previous number for next comparison
        else:
            # If the new number is smaller, end the game
            print("Thanks for playing!")
            print(f"Sequence length: {sequence}")
pass  # Exit the loop

if __name__ == "__main__":
    main()
