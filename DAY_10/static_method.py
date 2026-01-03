
# #! function creation
# class School:
#     sname='jes'
#     loc='hampi'
#     principal='nandakumar'
#     timing='9am - 4:30pm'

# def property(objname,name,age,id,bg):
#     objname.NAME=name
#     objname.AGE=age
#     objname.ID=id
#     objname.BG=bg

# st1=School()
# property(st1,'kanji',22,1234,'B+')
# print(st1.NAME,st1.AGE,st1.ID,st1.BG)


# st2=School()
# property(st2,'chetan',23,4567,'A+')
# print(st2.NAME,st1.AGE,st1.ID,st1.BG)

#~ __init__():


# class School:
#     sname='jes'
#     loc='hampi'
#     principal='nandakumar'
#     timing='9am - 4:30pm'

#     def __init__(self,name,age,id,bg):
#         self.NAME=name
#         self.AGE=age
#         self.ID=id
#         self.BG=bg

# st1=School('kanji',22,1234,'B+')
# print(st1.NAME,st1.AGE,st1.ID,st1.BG)


# st2=School('chetan',23,4567,'A+')
# print(st2.NAME,st1.AGE,st1.ID,st1.BG)


# class Company:
#     cname='TCS'
#     loc='mumbai'
#     CEO='kanji'
#     timing='9am - 4:30pm'

#     def __init__(self,name,age,id,salary,dept,mail):
#         self.NAME=name
#         self.AGE=age
#         self.ID=id
#         self.SALARY=salary
#         self.DEPT=dept
#         self.MAIL=mail

    


#     def change_id(self,new_id):
#         self.ID=new_id

#     def change_age(self,new_age):
#         self.AGE=new_age

#     def acess_obj(self):
#         print(self.NAME,self.AGE,self.ID,self.SALARY,self.DEPT,self.MAIL)


# emp1=Company('kanji',22,1234,'B+','IT','kanji@123')
# emp1.acess_obj()
# emp1.change_id(1292)
# emp1.change_age(23)
# emp1.acess_obj()


#! class method:-



class Company:
    cname='TCS'
    loc='mumbai'
    CEO='kanji'
    timing='9am - 4:30pm'

    def __init__(self,name,age,id,salary,dept,mail):
        self.NAME=name
        self.AGE=age
        self.ID=id
        self.SALARY=salary
        self.DEPT=dept
        self.MAIL=mail

    


    def change_id(self,new_id):
        self.ID=new_id

    def change_age(self,new_age):
        self.AGE=new_age

    def acess_obj(self):
        print(self.NAME,self.AGE,self.ID,self.SALARY,self.DEPT,self.MAIL)

    
      
    
    @classmethod
    def change_ceo(self,new_ceo):
        self.CEO=new_ceo

    @classmethod
    def acess_cls(cls):
        print(cls.cname,cls.loc,cls.CEO,cls.timing)

    @staticmethod
    def rules():
        print('1.you should be on time')

   
   
Company.change_ceo('chetan')
Company.acess_cls()
st1=Company('kanji',26,1223,30_000,'IT','kanji@123')

st1.acess_obj()
Company.rules()
st1.rules()


   


