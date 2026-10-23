num = 65
for i in range(1, 6):
    for j in range(1,6-i):
        print(" ", end=' ')
    for k in range(num, (i*2)+num-1):
        print(chr(k), end=' ')
    print()