# Accept age of a person. If age is less than 18, print minor otherwise Major.

age = int(input("Enter the age of the person :"))


def major_minor():
    if age > 18:
        print("You are in major category")

    else:
        print("You are in minor category")


major_minor()
