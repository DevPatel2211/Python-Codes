# Accept a year value from the user. Check whether it is a leap year or not.

year = int(input("Enter the year :"))


def leap():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is leap year")
            else:
                print(year, "is not leap year")
        else:
            print(year, "is leap year")
    else:
        print(year, "is not leap year")


leap()


# 2000,2004,2008 --> leap years(div by 4)(but 2000 also divisible by 100)(even though 2000 is also divisible by 400)
# 1900, 2100 --> not leap years (div by 4)(but also divisible by 100)(but not divisible by 400)
