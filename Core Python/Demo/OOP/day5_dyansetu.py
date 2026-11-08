# # Single Level
# class Empl:
#     def display(self):
#         print("I am from employeee class")

# class Hr(Empl):
#     pass
# h=Hr()
# h.display()

# # Multiple Level
# ## Base Class
# class Emp:
#     def display(self):
#         print("I am from employee class")
# ## Derived class from base class
# class Hr(Emp):
#     pass
# ## Derived class of derived class
# class JrHr(Hr):
#     pass
# # * Hirarchy Inheritance
# class Dev(Emp):
#     def display(self):
#         print("From Display dev")
# class SrDev(Emp):
#     print("From Display Srdev")
# jhr= JrHr()
# jhr.display()
# dev1 = Dev()
# dev1.display()
# dev2 = SrDev()
# dev2.display()


# * Multiple Inheritance
class mec:
    pass
    # def display(self):
    #     print("I am from mec")
class ele:
    def display(self):
        print("I am from ele")
class Mechatronix(mec, ele):
    pass
st = Mechatronix()
st.display()

