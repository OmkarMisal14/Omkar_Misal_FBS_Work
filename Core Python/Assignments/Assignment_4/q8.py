#  8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start = int(input("Entere a start number:"))
end = int(input("Entere a end number:"))
while start<end+1:
    if start%7==0 and start%5 == 0:
        print(start)
    start+=1