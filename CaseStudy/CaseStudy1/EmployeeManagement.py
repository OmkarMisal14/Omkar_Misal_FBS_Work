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
            print("Employee created successfully....")
    def displayEmployee(self):
        if not EmpMange.empDict:
            print("Employees not exits")
        else:
            for values in EmpMange.empDict.values():
                print(f"{values}")
    def searchEmployee(self):
        eId = int(input("Enter employee id: "))
        if eId in EmpMange.empDict:
            print(EmpMange.empDict[eId])
        else:
            print("Employee with this id is not found")

    def updateEmployee(Self):
        eId = int(input("Enter employee id: "))
        if eId in EmpMange.empDict: 
            newName = input("Enter New name of employee: ")
            EmpMange.empDict[eId].setName(newName)
            print("Name uploaded sucessfully ....")
    def deleteEmployee(self):
        eId = int(input("Enter employee id: "))
        if eId in EmpMange.empDict:
            print(f"Employee with id {eId} deleted successfully...")
            del EmpMange.empDict[eId]
        else:
            print("Employee not found ")
            return