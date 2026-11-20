from Hr import Hr
from Dev import Developer as dev
class EmpMange:
    empDict = {}
    def addEmployee(self):
        emp = None
        id = int(input("Enter Employee Id: "))
        if id in EmpMange.empDict:
            print("Employee with this id already exists.")
        else:
            name = input("Enter name of employee: ")
            sal = float(input("Enter salary of an Employee: "))
            role = int(input("Enter role:\n1 for Hr\n2 for developer\nEnter choice here- "))
            if role == 1:
                commission = float(input("Enter commision of Hr : "))
                emp = Hr(id, name , sal, commission)
            elif role == 2:
                bonus = float(input("Enter bonus of a developer: "))
                emp = dev(id, name, sal, bonus)
            else:
                print("Invalid Input.....")
            EmpMange.empDict[id] = emp
    def displayEmployee(self):
        if not EmpMange.empDict:
            print("Is empty?")
    def searchEmployee(self):
        print("Search ")

    def updateEmployee(Self):
        print("Update")

    def deleteEmployee(self):
        print("Delete")