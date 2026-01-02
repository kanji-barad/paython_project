class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_info(self):
        return f"car name is {self.brand} and model is {self.model}"
    
c1=Car('defender','legender')
print(c1.full_info())


    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

c1=ElectricCar('toyota','fortuner','85kWh')
print(c1.battery_size)
print(c1.full_info())