# Check whether a given number is divisible by 10 or not.

def divisible():
    a = int(input("Enter the number A : "))

    if a % 10 == 0:
        print(a, "is divisible by 10")

    else:
        print(a, "is not divisible by 10")


divisible()
