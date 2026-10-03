# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
marks1 = int(input("Enter subject1 marks: "))
marks2 = int(input("Enter subject2 marks: "))
marks3 = int(input("Enter subject3 marks: "))
marks4 = int(input("Enter subject4 marks: "))
marks5 = int(input("Enter subject5 marks: "))

total = ((marks1 + marks2 + marks3 + marks4 + marks5)/500)*100
if(total>=90):
    print("You got A grade.")
elif(total>=70 and total < 90):
    print("You got B grade.")
elif(total>=50 and total<70):
    print("You got C grade.")
elif(total>=40 and total<50):
    print("You passed.")
else:
    print("You have failed.")