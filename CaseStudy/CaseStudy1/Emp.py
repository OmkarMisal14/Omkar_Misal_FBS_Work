from abc import ABC, abstractmethod
class Employee(ABC):
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
    # @abstractmethod
    # def calSal(self):
    #     pass
