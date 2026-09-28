# Find the sum of three-digit number.
num = int(input("Enter a three digit number: "))
temp = num // 10

c1 = num % 10
c2 = temp // 10
c3 = temp % 10
total = c1 + c2 + c3
print(f"c1 is {c1}, c2 is {c2}, c3 is {c3}, temp is {temp}")
print("Total of three digit number is: ", total)
