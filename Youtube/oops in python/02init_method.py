class Defender:
    def __init__(self,userbrand,usermodel):
        self.brand=userbrand
        self.model=usermodel

d1=Defender('legender','defender')
print(d1.brand,d1.model)

class Defender:
    def __init__(self,userbrand,usermodel):
        self.brand=userbrand
        self.model=usermodel
    
    def display(self):
        return (f"brand name is {self.brand} and model is {self.model}")



d1=Defender('legender','defender')
print(d1.display())