#  9. WAP to print all numbers in a range divisible by a given number.
start = int(input("Enter a start number:"))
end = int(input("Enter a end number:"))
dvsble_num = int(input("Enter a divisible number: "))
while start<end+1:
    if start%dvsble_num==0:
        print(start)
    start+=1
    