# Write a program to reverse three-digit number.
num = int(input("Enter a Number: "))
l1 = num%10
temp = num//10
l2 = temp%10
l3 = temp//10
new_num = (l1*100) + (l2*10) + l3
print(f"Reversed number is {new_num}")