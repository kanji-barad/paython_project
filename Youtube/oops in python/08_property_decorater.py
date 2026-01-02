class Car:
    def __init__(self,model,brand):
        self.__model=model
        self.brand=brand

    @property #~ read only and its behave object calling type not methode type.
    def read_only(self):
        return self.__model
    
c1=Car('toyota','fortuner')
# print(c1.read_only()) #~ through an error method type not access 
print(c1.read_only)