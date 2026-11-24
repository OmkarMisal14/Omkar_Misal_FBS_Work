#  * Traditional way 
li = [2,3,4,5,6,67,7,8,44]
newList = []
for i in li:
    if(i%2 !=0):
        newList.append(i**2)

print(newList)

# ! Comprehension way
newLi = [i**2 for i in li if i%2!=0]
print(newLi)