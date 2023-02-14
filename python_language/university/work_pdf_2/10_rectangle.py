# Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter.

length = int(input("Length :"))
breadth = int(input("Breadth :"))


def rectangle():
    area = length*breadth
    perimeter = 2*(length+breadth)

    if area > perimeter:
        print("True")

    elif area == perimeter:
        print("Area and Perimeter both are same")

    else:
        print("False")


rectangle()
