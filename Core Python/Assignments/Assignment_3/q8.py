# 8. Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random as rd

usrnm = 'user1'
pswrd = 'pass1'

username = input("Enter username: ")
password = input("Enter password: ")

if(username == usrnm and password == pswrd):
    print("Please enter the captcha.")
    cptch = rd.randint(1000,9999)
    print(cptch)
else:
    print("Invalid credentials.")

captcha = int(input("Enter above captcha: "))
if(captcha == cptch):
    print("Your are authenticated.")
else:
    print("Authentication failed.(invalid captcha)")