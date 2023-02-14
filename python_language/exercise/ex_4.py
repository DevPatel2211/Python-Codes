# Write a program to check wheather you are pass or fail in your exam (50 or above in each subject and average 50 marks considered as a pass)

sub1 = int(input("Enter the Sub-1 marks :"))
sub2 = int(input("Enter the Sub-2 marks :"))
sub3 = int(input("Enter the Sub-3 marks :"))

total = sub1 + sub2 + sub3
avg = total / 3

if sub1 >= 50 and sub2 >= 50 and sub3 >= 50 and avg >= 50:
    print("You are pass")

elif sub1 > 100 or sub2 > 100 or sub3 > 100 or sub1 < 0 or sub2 < 0 or sub3 < 0 or total > 300 or avg > 100:
    print("You are lier, input real data")

else:
    print("You are fail")
