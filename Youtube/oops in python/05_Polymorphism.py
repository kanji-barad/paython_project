class Car:
    def __init__(self,brand,model):
        self.brand=brand 
        self.model=model

    def full_info(self):
        return f"car name is {self.__brand} and model is {self.model}"
    
    def fuel_type(self): #~ polymorphism method name is same but different behaviour
        return "petrol / disel"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self): #~ polymorphism method name is same but different behaviour
        return "Electric Charge"
    
c1=Car('toyota','fortuner')
print(c1.fuel_type()) #? output: petrol / disel

e1=ElectricCar('safari','tesla','85kWh')
print(e1.fuel_type()) #? output: Electric Charge





