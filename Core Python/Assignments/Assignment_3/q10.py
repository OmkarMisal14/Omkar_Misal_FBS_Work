#  10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gender = input("Enter gender(F/M): ")
age  = int(input("Enter your age: "))
if( gender=='M'):
    if(age>=21):
        print("Boy is eligible to marriage!")
    else:
        print("Boy is not eligible to marriage")

else:
    if(age>=18):
        print("Girl is eligible to marriage!")
    else: 
        print("Girl is not eligible to marriage")
