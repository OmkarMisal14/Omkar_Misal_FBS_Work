# * Traditional Way
li = [3,4,5,1,2]
newList = []
for a in li:
    newList.append(20+a)
print(newList)
# ! Comprehension way 
newLi = [20+a for a in li]
print(newLi)
