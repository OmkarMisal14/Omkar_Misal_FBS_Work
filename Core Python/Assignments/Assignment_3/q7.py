# 7. Write a program to check if user has entered correct userid and password.
usrnm = 'user1'
pswrd = 'pass1'

username = input("Enter username: ")
password = input("Enter password: ")

if(username == usrnm and password == pswrd):
    print("Login success.")
else:
    print("Invalid credentials.")