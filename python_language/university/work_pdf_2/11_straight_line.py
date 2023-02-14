# Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line

# if the area of the triangle becomes zero then we say that 3 points are in straight line

def straight():
    x1 = int(input("Enter X1 :"))
    x2 = int(input("Enter X2 :"))
    x3 = int(input("Enter X3 :"))
    y1 = int(input("Enter Y1 :"))
    y2 = int(input("Enter Y2 :"))
    y3 = int(input("Enter Y3 :"))

    area = x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)

    if area == 0:
        print("All 3 points are in same line")

    else:
        print("all 3 points are not in same line")


straight()
