num = int(input("Enter a num: "))
# Linear Searching
li =[1,2,3,4,5,6]
for i in li:
    if(i == num):
        print("Num found")
        break
else:
    print("Num not found")