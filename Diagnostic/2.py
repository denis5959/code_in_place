# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100
def main():
    for i in range(1, MAX_NUMBER + 1):
        if i%2 == 0:
            print(str(i) + " is even")
        else:
            print(str(i) + " is odd")
    pass

if __name__ == "__main__":
    main()
