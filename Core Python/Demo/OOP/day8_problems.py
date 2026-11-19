# WAP to add twol integers
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print(num1+num2)

# WAP to add two Strings 
# s1 = input("Enter string 1: ")
# s2 = input("Enter string 2: ")
# print(s1+" "+s2)

# WAP to add 2 lists
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9]
# print(l1+l2)

# WAP to add 2 time object
class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __add__(self, other):
        t_sec = self.sec + other.sec
        c_sec = t_sec//60
        t_sec = t_sec%60
        t_min = self.min+other.min+t_sec
        c_min = t_min //60
        t_min = t_min%60
        t_hr = self.hr + other.hr + c_min
        return Time(t_hr, t_min,t_sec)
    # def __add__(self, other):
    #     t_hr = self.hr+other.hr
    #     t_min = self.min+other.min
    #     t_sec = self.sec+other.sec
    #     return Time(t_hr, t_min,t_sec)
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"

t1 = Time(9,55,59)
t2 = Time(4, 59,55)
print(t1+t2)