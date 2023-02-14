# Make a reverse multiplication table

# number = input("Enter the number :")
# number = int(number)
# count = 10


# while count > 0:
#     product = number * count
#     print(number, "x", count, "=", product)
#     count -= 1


number = int(input("Enter the number :"))

for count in range(1, 11):
    product = number * count
    print(number, "x", count, "=", product)
