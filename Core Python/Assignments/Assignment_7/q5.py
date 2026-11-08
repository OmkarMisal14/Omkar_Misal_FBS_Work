for i in range(1, 6):
    for j in range(1, 6-i):
        print(" ", end=' ')
    for g in range(1, 6):
        if i == 1 or j == 1 or j == i:
            print(i, end=' ')
        else:
            print(" ", end=' ')
    print()