def main():
    print("Enter a sequence of non-decreasing numbers.")
    previous_number = float(input("Enter num: "))
    sequence = 1

    while True:
        secondary_number = float(input("Enter num: "))
        if (secondary_number>= previous_number):
            sequence += 1
            previous_number = secondary_number
        else:
            print("Thanks for playing!")
            print(f"sequence Length: {sequence}")
pass 

if __name__ == "__main__":
    main()
