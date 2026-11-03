# Define
s1 = "Virat"
print(s1)
s2 = "Veerat"
print(s2)

s1 = "Firstbit Solutions"
# Traversing (Direct)
for ch in s1:
    print(ch, end=' ')

# Traversing(Indirect)
for ch in range(len(s1)):
    print(s1[ch], end=' ')

# Index accessing
print()
print(s1[9])