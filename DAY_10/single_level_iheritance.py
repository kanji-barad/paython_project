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

  

   
class Updated_company(Company):
    company_code=12345

    def __init__(self,name,age,id,salary,dept,mail,adhar,pan_card):
        self.NAME=name
        self.AGE=age
        self.ID=id
        self.SALARY=salary
        self.DEPT=dept
        self.MAIL=mail
#~ -------------------------------------
        self.adhar=adhar
        self.pan_card=pan_card

    def acess_obj(self):
        print(self.NAME,self.AGE,self.ID,self.SALARY,self.DEPT,self.MAIL,self.adhar,self.pan_card)
    
    @classmethod
    def acess_cls(cls):
        print(cls.cname,cls.loc,cls.CEO,cls.timing,cls.company_code)

c1=Updated_company('kanji',23,1234,20_000,'IT','kanji@123',442332057416,'CFTPJ5106A')
c1.acess_obj()
c1.acess_cls()


   


