# 13. Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

n = int(input("Enter electricity unit: "))
unit = n
c1 = 0; c2 =0 ; c3 = 0 ; c4 = 0
if(n<=50):
    c1 = n*.5
elif(n>50 and n<=150):
    c1 = 50*0.5
    n = n-50
    c2 = n*0.75
elif(n>150 and n<=250):
    c1 = 50*0.5
    n = n-50
    c2 = 100*0.75
    n = n-100
    c3 = n*1.2
elif(n>250):
     c1 = 50*0.5
     n = n-50
     c2 = 100*0.75
     n = n-100
     c3 = 100*1.2
     n = n-100
     c4 = n*1.5

total = (c1 + c2 + c3+ c4 )*0.2
total = (c1 + c2 + c3+ c4 )+total
print("Total price needs to pay is", total)

# Improvised versionn
n = unit
bill = 0
if n<=50:
    bill = n*.5
elif n<=150:
    bill = 50*0.5
    n = n-50
    bill+=n*0.75
elif n<=250:
    bill = 50*.5
    n = n-50
    bill+= 100*.75
    n= n-100
    bill += n*1.2
else:
    bill = 50*.5
    n = n-50
    bill+= 100*.75
    n= n-100
    bill += 100*1.2
    n = n-100
    bill += n*1.5

total =( bill *.2)+bill
print("Total price needs to pay is", total)
    
