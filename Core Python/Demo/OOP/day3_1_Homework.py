class PlacedStudent:
    def __init__(self, frn, name, company_name, batch):
        self.frn = frn
        self.name = name
        self.company_name = company_name
        self.batch = batch
    def getFrn(self):
        return self.frn
    def setFrn(self, frn_no):
        self.frn = frn_no
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getCompanyName(self):
        return self.company_name
    def setCompanyName(self, compny_name):
        self.name = compny_name
    def getBatch(self):
        return self.batch
    def setBatch(self, batch):
        self.batch = batch

class Student:
    def __init__(self, frn, name, batch):
        self.frn = frn
        self.name = name
        self.batch = batch
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