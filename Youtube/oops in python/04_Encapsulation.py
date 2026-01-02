class Car:
    def __init__(self,brand,model):
        self.__brand=brand #~ private variable
        self.model=model

    def full_info(self):
        return f"car name is {self.__brand} and model is {self.model}"
    
    def set_brand(self,new): #~ setter method
        self.new=new
        self.__brand=self.new
        return self.__brand
    
    def get_brand(self): #~ getter method
        return f"{self.__brand}!"
    
   
    
    
c1=Car('defender','legender')
print(c1.full_info())


    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

c1=ElectricCar('toyota','fortuner','85kWh')
print(c1.battery_size)
print(c1.full_info())
# print(c1.__brand) #~ error through because private varible not accessed to the outside of class
print(c1.get_brand()) #~ call getter metod
print(c1.set_brand('BMW')) #~ call setter method / it is used to modify the private variable
