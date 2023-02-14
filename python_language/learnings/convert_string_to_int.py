#User input is always on string, we can not able to get input in integer/float directly from the user

print("-------------------------------------------------------")

print("==> String Output")
number1 = input("Enter the number : ")
print(number1)
print(type(number1))

print("-------------------------------------------------------")

# 1st --> input from user in a string format
# 2nd --> convert string format input into int/float format
# 3rd --> get/generate output

print("==> Int Output 1.0")

number2 = input("Enter the number : ")
number2 = int(number2)
print(number2)
print(type(number2))

print("-------------------------------------------------------")

print("==> Int Output 2.0")

number3 = int(input("Enter the number : "))
print(number3)
print(type(number3))

print("-------------------------------------------------------")