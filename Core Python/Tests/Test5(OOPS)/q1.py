from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,person):
        self.person = person

    @abstractmethod
    def calToll(self):
        pass

class twoWheelers(Vehicle):
    def calToll(self):
        if self.person>2:
            total = (self.person-2)*10
        else:
            total = 0
        return 20+total

class threeWheelers(Vehicle):
    def calToll(self):
        if self.person>3:
            total = (self.person-3)*20
        else:
            total = 0
        return 30+total

class fourWheelers(Vehicle):
    def calToll(self):
        if self.person >4:
            total = (self.person-4)*40
        else:
            total = 0
        return 40+total

class heavyVehicle(Vehicle):
    def calToll(self):
        if self.person>6:
            total = (self.person-6)*100
        else:
            total=0
        return 60+total


while True:
    print("Toll Tax")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Two Wheeler")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 5):
        print("Thank You!!")
        break
    if choice not in [1,2,3,4,5]:
        print("Invalid choice.")
        continue
    p = int(input("Enter number of persons: "))
    if p <=0:
        print("Number of persons should be greater than 0")
        continue

    if(choice == 1):
        o = twoWheelers(p)
        print("Total tax value is ", o.calToll())
    elif choice == 2:
        o = threeWheelers(p)
        print("Total tax value is ", o.calToll())
    elif choice == 3:
        o = fourWheelers(p)
        print("Total tax value is ", o.calToll())
    elif choice == 4:
        o = heavyVehicle(p)
        print("Total tax value is ", o.calToll())