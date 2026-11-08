# Reverse sentence without reversing the word
s1  = "I am good"
start = 0
end = 0
li = []
for i in s1:
    if(i == ' '):
        end = i
        li.append(s1(start:end:1))
        start = i+1