# Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if te sum of all the three angles is equal to 180 degrees.

a = float(input("Enter the angle 1 :"))
b = float(input("Enter the angle 2 :"))
c = float(input("Enter the angle 3 :"))


def triangle():
    sum = a+b+c
    if sum == 180:
        print("The Triangle is valid")

    else:
        print("The triangle is not valid")


triangle()
