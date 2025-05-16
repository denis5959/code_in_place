import random
def main():
    print("Khansole Academy")
    first = random.randint(10,99)
    second = random.randint(10,99)
    print(f"What is {first} + {second}?")
    addition = first + second
    answer = int(input("Your answer: "))
    if addition == answer:
        print("Correct!")
    else:
        print("Incorrect.")  
        print(f"The expected answer is {addition}")

if __name__ == '__main__':
    main()
