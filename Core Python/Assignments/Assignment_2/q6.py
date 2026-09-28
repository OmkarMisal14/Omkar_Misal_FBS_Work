# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.
base_salary = float(input("Enter Current Salary: "))
new_salary = (base_salary*(10/100)) + (base_salary*(12/100))+(base_salary *(15/100)) + base_salary
print("New/Update salary is ", new_salary)