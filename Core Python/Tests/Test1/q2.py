# 2. Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate:"))
time = int(input("Enter time in years: "))
smpl_intrst = (principal*(rate)*time)/100
print("Simple instrest is:", smpl_intrst)
