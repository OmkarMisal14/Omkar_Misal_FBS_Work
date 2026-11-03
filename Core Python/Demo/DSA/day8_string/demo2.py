s1 = "firstbit solutions"
res =""
for i in range(len(s1)-1,-1, -1):
    res +=s1[i]
print(res)
rev = ""
for ch in s1:
    rev = ch+rev
print(rev)