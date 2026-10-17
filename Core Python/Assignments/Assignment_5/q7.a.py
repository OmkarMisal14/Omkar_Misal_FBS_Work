# a. 1! + 2! + 3! + 4! + .....n!
n = int(input("Enter n number: "))
sum = 0
for i in range(1, n+1):
    total = i
    for j in range(i, 1,-1):
        total *= (j-1)
    sum+=total
print("The total is", sum)