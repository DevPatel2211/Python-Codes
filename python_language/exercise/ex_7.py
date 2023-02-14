# Find the sum of numbers of 1 to 100

n = int(input("Enter the Number to Find the sum of the number :"))

sum = 0

for count in range(1, n+1):
    sum = sum + count

print(sum)
