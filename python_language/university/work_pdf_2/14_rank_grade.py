# Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <== 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:
# Marks Range Grade
# Absent NA

# 0 – 39 F
# 40 – 44 P
# 45 – 49 C
# 50 – 54 B
# 55 – 59 B+
# 60 – 69 A
# 70 – 79 A+
# 80 – 100 O


def result():
    a = float(input("Enter the Numbers of Subject-1 :"))
    b = float(input("Enter the Numbers of Subject-2 :"))
    c = float(input("Enter the Numbers of Subject-3 :"))

    total = a + b + c
    avg = (a + b + c) / 3

    if a <= 39 and b <= 39 and c <= 39:
        print("You are fail")

    else:
        print("You are pass")

    if avg >= 0 and avg <= 39:
        print("Grade - F")

    if avg >= 40 and avg <= 44:
        print("Grade - P")

    if avg >= 45 and avg <= 49:
        print("Grade - C")

    if avg >= 50 and avg <= 54:
        print("Grade - B")

    if avg >= 55 and avg <= 59:
        print("Grade - B+")

    if avg >= 60 and avg <= 69:
        print("Grade - A")

    if avg >= 70 and avg <= 79:
        print("Grade - A+")

    if avg >= 80 and avg <= 100:
        print("Grade - O")


result()
