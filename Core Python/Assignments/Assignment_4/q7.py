#  7. WAP to print all integers upto n that aren’t divisible by 2 and 3.
num = int(input("Enter a nubmer: "))
i = 1
while i<num+1:
    if( i%2==0 or i%3==0):
        i+=1
        continue
    print(i)
    i+=1