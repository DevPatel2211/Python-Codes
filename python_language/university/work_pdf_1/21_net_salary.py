gross_salary = float(input("Enter the Gross salary = "))
allowance = gross_salary * 0.10
deduction = gross_salary * 0.03

net_salary = gross_salary + allowance - deduction

print("Net salary = ", net_salary)
