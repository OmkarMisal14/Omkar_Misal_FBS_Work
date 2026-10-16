# for i in range(1, 6):
#     for j in range(1, i):
#         print(" ", end=' ')
#     for g in range(5, i-1, -1):
#         print("*", end=' ')
#     print()

for i in range(1, 6):
    for j in range(1, i+1):
            print('*', end=' ')
    for h in range(6,0,-2):
           print(" ", end=' ')
    for g in range(i, 0, -1):
           print("*", end=' ')
    print()