#  6. Write a program to calculate profit or loss.
cost_price = float(input("Enter your cost price: "))
sell_price = float(input("Enter your selling price: "))

if(cost_price< sell_price):
    print("You have profit of Rs.", cost_price-sell_price)
elif(cost_price== sell_price):
    print("You have nor profit not loss")
else:
    print("You have loss of Rs.", sell_price-cost_price)