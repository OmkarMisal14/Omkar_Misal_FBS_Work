class Student:
    sCount = 0
    def __init__(self, frn, name, batch):
        self.frn = frn
        self.name = name
        self.batch = batch
        Student.sCount +=1
    def getFrn(self):
            return self.frn
    def setFrn(self, frn_no):
        self.frn = frn_no
    def getName(self):
        return self.name
    def setName(self, nme):
        self.name = nme
    def getBatch(self):
        return self.batch
    def setBatch(self, btch):
        self.batch = btch
    def display(self):
         print(f"frn:{self.frn}, name: {self.name}, batch = {self.batch}")

class PlacedStudent(Student):
    def __init__(self, frn, name, batch, company_name):
           super().__init__(frn, name, batch)
           self.company_name = company_name
      
    def getCompanyName(self):
        return self.company_name
    def setCompanyName(self, compny_name):
        self.name = compny_name
    def display(self):
        super().display()
        print(f"Company Name = {self.company_name}")   
        print(f"Student Count is {super().sCount}")   

s1 = Student(1, "Ram","Sept Python" )
s2 = PlacedStudent(2, "Shyam", "Aug Python", "TCS")
s1.display()
s2.display()