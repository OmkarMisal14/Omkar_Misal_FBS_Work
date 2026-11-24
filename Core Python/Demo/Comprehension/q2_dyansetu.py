# Wap to create list of vowels present in a list 
# * Traditional way
s = "I am good in coding"
li = []
for i in s: 
    if i in "aeiouAEIOU":
        li.append(i)
print(set(li))
# ! Nested Comprehension way 
newLi = {i  for i in s if i in "aeiouAEIOU" }
print(newLi)