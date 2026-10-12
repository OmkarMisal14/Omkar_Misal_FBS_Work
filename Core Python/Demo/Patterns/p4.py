for i in range(1, 6):
    for j in range(i, 6):
        print(" ", end=' ')
    for g in range(1, i+1):
        print("*", end=' ')
    print()