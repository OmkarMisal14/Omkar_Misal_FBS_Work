dir = "NWNNEENNESE"
x = 0
y = 0

for i in dir:
    if i =="N":
        y +=1
    elif i == "S":
        y-=1
    elif i=="E":
        x+=1
    elif i == "W":
        x-=1
    else:
        print("Invalid Input")
else:
    res = ((x**2)+(y**2))**.5
    print("Total distance is", res)