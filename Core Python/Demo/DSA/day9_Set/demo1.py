# Declaration
s = {11,2,2,3,11,5,7,7}
print(s)

# Traversing
# Direct Traversing
for i in s:
    print(i)
# Indirect traversing is not possible

# Operations of set
s1 = {1,2,3,4,5,6}
s2 = {11,12,3,4,7,6}
# Prints all the elements from both set
print(s1.union(s2))
# Prints only common elements from both set
print(s1.intersection(s2))
# Prints only uncommon elements from s1
print(s1.difference(s2))
# Prints only uncommon elements from s2
print(s2.difference(s1))

ss = {1,2,3,4,5,6,7}
print(type(ss))
sf = frozenset(ss)
print(type(sf))