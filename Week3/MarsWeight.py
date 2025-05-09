MARS_CONSTANT = 0.378

def main():
    weight_earth = input("Enter a weight on Earth: ")
    weight_earth = MARS_CONSTANT*int(weight_earth)
    print("The equivalent weight on Mars: " + str(weight_earth))
    # Fill this function out!
    pass

if __name__ == "__main__":
    main()
