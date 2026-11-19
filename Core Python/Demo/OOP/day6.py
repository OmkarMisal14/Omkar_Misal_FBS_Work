class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def getId(self):
        return self.id
    def setId(self, emp_id):
        self.id = emp_id
    def getName(self):
        return self.name
    def setName(self, emp_name):
        self.name = emp_name
    def getSalary(self):
        return self.salary
    def setSalary(self, emp_salary):
        self.salary = emp_salary
    def __str__(self):
        return f"Id: {self.id} Name:{self.name} Salary: {self.salary}"
    def calSal(self):
        print(f"Total Employee salary is :{self.salary}")

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
        

class Developer(Employee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self.bonus = bonus
    def getbonus(self):
        return self.bonus
    def setbonus(self, dev_bonus):
        self.bonus = dev_bonus
    def display(self):
        return super().__str__+f" Developer Bonus: {self.bonus}"


emp = Employee(1, "Rohit Misal", 150000)
hr = Hr(1, "Rohit Misal", 150000, 25000)
dev = Developer(1, "Rohit Misal", 150000, 30000)
print(emp)
print(dev)