# 1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.
usrnm = "Admin"
pswrd = "Admin@2"
i = 1
while i<=3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if(username == usrnm and password == pswrd):
        print("Login success.")
        break
    else:
        print("Invalid Credentials.")

    i+=1