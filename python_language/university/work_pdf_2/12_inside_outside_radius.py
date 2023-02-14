# Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )


def radius():
    r = float(input("Enter the radius :"))
    x = float(input("Enter the center coordinates x :"))
    y = float(input("Enter the center coordinates y :"))
    x1 = float(input("Enter the point coordinates x1 :"))
    y1 = float(input("Enter the point coordinates y1 :"))

    value = pow(x-x1, 2) + pow(y-y1, 2)

    if pow(r, 2) < value:
        print("The point lies outside the circle")

    if pow(r, 2) == value:
        print("The point lies on the circle")

    if pow(r, 2) > value:
        print("The point lies inside the circle")


radius()
