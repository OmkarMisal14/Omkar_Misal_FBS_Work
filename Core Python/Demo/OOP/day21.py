class Student:
    def __init__(self,frn, name, batch_name):
        self.frn = frn
        self.name = name
        self.batch_name = batch_name
    def getRoll(self):
        return self.frn
    def getName(self):
        return self.name
    def getbatch_name(self):
            return self.batch_name
    def setFrn(self, frn):
         self.frn = frn
    def setName(self, name):
             self.name = name
    def setBatch_name(self, batch_name):
                 self.batch_name = batch_name
    
    def display(self):
         print(f"Roll NO: {self.frn}, name:{self.name}, batch_name: {self.batch_name}")

s = Student(1, "Rahul", 95)
s.display()   
print(s.getName())