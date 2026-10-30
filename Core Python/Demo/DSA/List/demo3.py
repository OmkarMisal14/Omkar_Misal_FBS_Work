# li = [7,18, 45, 1, 33, 66]
li = [1,2,3,4]
total =0
# Direct Traversing
# for i in li:
#     if i%2!=0:
#         total+=i
5
# Indexing Traversing
for i in range(len(li)):
    if li[i]%2!=0:
        total+=li[i]

print("Sum of even numbers in list is:", total)