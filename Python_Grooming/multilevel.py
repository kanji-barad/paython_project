# class Grandfather:
#     def __init__(self, grandfather_name):
#         self.grandfather_name = grandfather_name

#     def display(self):
#         return self.grandfather_name


# class Father(Grandfather):
#     def __init__(self, grandfather_name, father):
#         super().__init__(grandfather_name)
#         self.father = father

#     def display(self):
#         var = super().display()
#         return self.father + " " + var


# class Son(Father):
#     def __init__(self, grandfather_name, father, son):
#         super().__init__(grandfather_name, father)
#         self.son = son

#     def display(self):
#         var = super().display()
#         return self.son + " " + var


# c1 = Son('jethabhai', 'jadavbhai', 'kanji')
# print(c1.display())


# class A:
#     c=10
#     @staticmethod
#     def demo():
#         return 'I am from A class'
    
# class B:
#     Z=45
#     @staticmethod
#     def demo():
#         return 'I am from B parent Class'
    
# class c(A,B):
#     # @staticmethod
#     # def demo():
#     #     return 'I am from C Child Class'
#     pass


# c1=c()
# print(c1.demo())

# class C1:
#     a=10
#     def __init__(self,value1):
#         self.value1=value1
#     @staticmethod
#     def demo():
#         return 'i am from calss c1'
    
# class C2(C1):
#     b=45
#     def __init__(self,value2):
#         self.value2=value2
#     @staticmethod
#     def demo():
#         return 'i am from calss c2'
    
# class C3(C1):
#     d=20
#     def __init__(self,value3):
#         self.value3=value3
#     @staticmethod
#     def demo():
#         return 'i am from calss c3'
    
# class C4(C3,C2):
#     d=20
#     def __init__(self,value2,value4):
#         super().__init__(value2)
#         self.value4=value4
#     @staticmethod
#     def demo():
#         return 'i am from calss c4'

    
# c1=C4(12,45)
# print(c1.demo())


class Bank:
    bravch_manager="mr meru"
    branch='ahemdabad'

    def __init__(self,name,ac_no,balance):
        self.name=name
        self.ac_no=ac_no
        self.__balance=balance
    
    @classmethod
    def display(cls):
        return cls.bravch_manager,cls.branch
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_balance):
        self.new_balance=new_balance
        self.__balance+=new_balance
        return self.__balance

b1=Bank('kanji',123,12000)
print(b1.get_balance())
print(b1.set_balance(8000))
print(b1.get_balance())
print(b1.display())
