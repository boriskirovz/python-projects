class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self):
        print(self.brand, self.model, self.year)

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type=fuel_type
    
    def info(self):
        super().info()  
        print("Fuel:", self.fuel_type)

car1 = Car("BMW", "e60", 2009, "benzin")
car2 = Car("Opel", "Insignia", 2016, "dizel")
car3 = Car("VW", "Golf", 2012, "gas")

car1.info()
car2.info()
car3.info()