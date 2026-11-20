from Emp import Employee
class Hr(Employee):
    def __init__(self, id, name, salary, commision):
        super().__init__(id, name, salary)
        self.commision = commision
    def getCommision(self):
        return self.commision
    def setCommision(self, hr_comision):
        self.commision = hr_comision
    def __str__(self):
        return super().__str__+f"Hr Commision: {self.commision}"