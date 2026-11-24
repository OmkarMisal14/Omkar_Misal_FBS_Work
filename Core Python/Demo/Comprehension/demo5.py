li = [2,3,14,17, 22]
# * Traditional way
newList = []
for i in li:
    if i%2==0:
        newList.append("even")
    else:
        newList.append("odd")
print(newList)

# ! Comprehension way
newLi = ["even" if i%2==0 else "odd" for i in li]
print(newLi)