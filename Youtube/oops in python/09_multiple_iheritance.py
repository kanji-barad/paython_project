class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_info(self):
        return f"car name is {self.brand} and model is {self.model}"
    



    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

class Battery:
    def battery_info(self):
        return 'battery'

class engine:
    def engine_info(self):
        return 'engine'

class Electric_car_2(Car,Battery,engine):
    pass

e1=Electric_car_2('toyota','fortuner')
print(e1.battery_info())
print(e1.engine_info())