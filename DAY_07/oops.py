
#! class creation
# class Company:
#     # class properties
#     c_name='TCS'
#     Director='Bhavin'
#     Address='Ahemdabad'

# #~ object creation
# e1=Company()

# #~ using class name
# print(Company.Address)

# #~ using object name
# print(e1.Address)


class Student:
    sname='D.M Barad'
    Address="Ghushiya Gir"
    District='Gir somnath'
    Principal='G.P vala'
    Owner='Jasubhai Barad'

print(Student.Owner)

s1=Student()
s1.Owner='Shailesh Barad'
print(s1.Owner)

Student.Address='Talala Gir'
print(Student.Address)
print(s1.Address)


