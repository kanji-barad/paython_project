class Car:

    total_car=0
    def __init__(self,brand,model):
        self.brand=brand 
        self.model=model
        Car.total_car+=1 #~ using car class access variable

    def full_info(self):
        return f"car name is {self.brand} and model is {self.model}"
    
    def fuel_type(self):
        return "petrol / disel"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self): 
        return "Electric Charge"
    
c1=Car('toyota','fortuner')
print(c1.fuel_type()) 

e1=ElectricCar('safari','tesla','85kWh')
print(e1.fuel_type()) 

test=Car.total_car #~ access calss variable
print(test)








