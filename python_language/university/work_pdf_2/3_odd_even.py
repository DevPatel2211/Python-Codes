# Check whether a given number is odd or even.

def fun():
    a = int(input("Enter the Number A :"))

    if a == 0:
        print(a, "is neither even nor odd")

    elif a % 2 == 0:
        print(a, "is even number")

    else:
        print(a, "is odd")


fun()
