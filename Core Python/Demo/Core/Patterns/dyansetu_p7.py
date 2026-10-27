# for i in range(1, 6):
#     for j in range(1, 7-i):
#         print(i, end=' ')
#     print()
for i in range(1, 6):
    for j in range(5, i-1, -1):
        print(i, end=' ')
    print()