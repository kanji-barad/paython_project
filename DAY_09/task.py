
#! task create a bank class and 4 class member ,5 object member 2 class metod and 2 object metod creat using oops concept.
class Bank:
    bank_name='HDFC BANK'
    ifsc_code='HDFC1203'
    address='Sola Bridge'
    manager='yuvraj barad'
    
    def __init__(self,cname,ac_no,ac_type,mo_no,e_mail):
        self.cname=cname
        self.ac_no=ac_no
        self.ac_type=ac_type
        self.mo_no=mo_no
        self.e_mail=e_mail

    @classmethod
    def cls_show(cls):
        print(f"bank name is {cls.bank_name} \nifsc code is {cls.ifsc_code} \naddress is {cls.address} \nand branch manager is {cls.manager}\n")
    
    @classmethod
    def cls_manager_modify(cls,new_val):
        cls.manager=new_val
        

    def obj_modify(self,new_val):
        self.mo_no=new_val

    def obj_show(self):
        print(f"costomer name is {self.cname} and ac_no is {self.ac_no}, mobile number is {self.mo_no} and email is {self.e_mail}")

    @staticmethod
    def rules():
        print('lunch time is 1:00 to 2:00')


#! object member modify & access
b1=Bank('kanji','31410','saving account',7984844987,'kanji@123')
b1.obj_show()

b2=Bank('chetan','31420','current account',7984844877,'chetan@8232')
b1.obj_show()

b3=Bank('vishal','31450','personal account',7984222987,'vishal@1292')
b1.obj_show()

b4=Bank('hardik','31810','saving account',79848222423,'hardik@0007')
b1.obj_show()

b1.obj_show()
b1.obj_modify('9879336448')
b1.obj_show()

#~ class member modify & access

b1.cls_show()
b1.cls_manager_modify('prabhat')
b1.cls_show()

Bank.rules()
b1.rules()





    