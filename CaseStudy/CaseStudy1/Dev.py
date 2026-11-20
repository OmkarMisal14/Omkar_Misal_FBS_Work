from Emp import Employee
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
