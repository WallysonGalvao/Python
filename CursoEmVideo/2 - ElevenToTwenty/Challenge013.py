"""Salary readjustment"""

# Challenge 013
# Make an algorithm that read the employee's salary and show its new salary, with 15% of increase.
print("Challenge 013")
print("Make an algorithm that read the employee's salary and show its new salary, with 15% of increase.")
salaryOfEmployee = float(input("What is the employee's salary ? $"))
newSalary = salaryOfEmployee + (salaryOfEmployee * 15 / 100)
print("An employee earning ${}, with a 15% raise, is getting ${}".format(salaryOfEmployee, newSalary))
