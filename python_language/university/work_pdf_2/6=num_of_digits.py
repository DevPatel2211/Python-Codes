# Accept a number from the user. And print number of digits in it.

number = int(input("Enter the number :"))
count = 0


def fun():

    while number ! 0:
        number = number//10
        count = count + 1

    print("The input number's digit is", str(count))


fun()
