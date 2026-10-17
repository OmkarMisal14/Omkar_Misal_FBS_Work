# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
p_num = int(input("Enter number of passenger: "))
ticket_price = 300
sum = 0
while p_num>0:
    age = int(input("Enter age of passenger: "))
    if(age<12):
        sum+=(ticket_price-(ticket_price*0.3))
        print(sum, "this is if else sum")
    elif(age>59):
        sum+=(ticket_price-(ticket_price*0.5))
        print(sum, "this is if else sum")
    else:
        sum+=ticket_price
        print(sum, "this is if else sum")
    p_num-=1
print(f"Total amount: {sum}")