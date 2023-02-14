# Print largest and smallest values out of three.

def fun():
    a = int(input("Enter the Number A :"))
    b = int(input("Enter the Number B :"))
    c = int(input("Enter the Number C :"))

    if a > b and a > c:
        print(a, "is the largest number")

    elif b > a and b > c:
        print(b, "is the largest number")

    elif c > a and c > b:
        print(c, "is the largest number")

    else:
        print(a, b, c, "all are equal")


fun()
