class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    def getId(self):
        return self.id
    def setId(self, id):
        self.id=id
    def setname(self, name):
        selfname = name
    def getName(self):
        return self.name
    def getSal (self):
        return self.sal
    def setSalI(self, sal):
        self.sal = sal
        

    def display(self):
        print(f"This is id {self.id}, name: {self.name}, sal:{self.sal}")

e1=Employee(101, 'Sachin', 12345)
e1.display()
print(e1.getId())
print(e1.sal())