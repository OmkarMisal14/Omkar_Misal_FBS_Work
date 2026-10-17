# 2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.
st_count = int(input("Enter count of student: "))
while st_count>0:
    sub1 = float(input("Enter subject 1 marks: "))
    sub2 = float(input("Enter subject 2 marks: "))
    sub3 = float(input("Enter subject 3 marks: "))
    sub4 = float(input("Enter subject 4 marks: "))
    sub5 = float(input("Enter subject 5 marks: "))
    total = sub1+sub2+sub3+sub4+sub5
    per =( total/500)*100
    print("Percentage is", per)
    st_count-=1