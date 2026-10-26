# 4. Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.
len = int(input("Enter Length: "))
width = int(input("Enter height: "))
cost = int(input("Enter painting cost: "))

total_cost = 4*len*width*cost
print("Total cost is", total_cost)
