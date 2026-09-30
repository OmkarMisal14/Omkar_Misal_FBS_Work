# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
num = int(input("Enter a number"))
n2000 = num //2000
n = num%2000
n500 = n// 500
n = n%500
n200 = n//200
n = n%200
n100 = n//100
n = n%100
n50 = n// 50
n = n%50
n20 = n//20
n = n%20
n10 = n//10
n = n%10
n5 = n//5
n = n%5
n2 = n//2
n = n%2
n1 = n
print(f"we need 2000:{n2000}, 500:{n500}, 200:{n200}, 100:{n100}, 50:{n50}, 20:{n20}, 10:{n10}, 5:{n5}, 2:{n2} and 1:{n1}")
