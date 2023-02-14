# Print largest and smallest values out of two.

def fun():
    a = int(input("Enter the Number A :"))
    b = int(input("Enter the Number B :"))
    if a > b:
        print(a, "is the largest number.")
        print(b, "is the smallest number.")
    elif a == b:
        print(a, "and", b, "are same")
    else:
        print(b, "is the Largest number")
        print(a, "is the Smallest number")


fun()
