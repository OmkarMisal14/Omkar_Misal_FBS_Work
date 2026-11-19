from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand , color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"Name:{self.brand}, Color:{self.color}"
    @abstractmethod
    def brake(self):
        pass
class Car(Vehicle):
    def __init__(self,brand, color, sunroof):
        super().__init__(brand, color)
        self.sunroof = sunroof
    def __str__(self):
        return super().__str__()+f" Sunroof Available:{self.sunroof}"
    def brake(self):
        print("Drum brake of a car")

c1 = Car("Maruti suzuki", "white", "Yess")
c1.brake()
print(c1)