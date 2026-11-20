from EmployeeManagement import EmpMange
class Main:
    def login(self):
        usr = input("Enter Username: ")
        pas = input("Enter Password: ")
        if usr == 'admin' and pas == '1234':
            pass 
    def showMenu(self):
        while True:
            print("1. Add Employee")
            print("2. Display Employee")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit......")
            em = EmpMange()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                em.addEmployee()
            elif choice == 2:
                em.displayEmployee()
            elif choice == 3:
                em.searchEmployee()
            elif choice == 4:
                em.updateEmployee()
            elif choice == 5:
                em.deleteEmployee()
            elif choice == 6:
                print("Thank You...")
                break
            else:
                print("Invalid choice....")

m = Main()
m.showMenu()