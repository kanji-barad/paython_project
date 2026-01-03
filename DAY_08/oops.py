class Company:
    # class properties
    c_name='TCS'
    Director='Bhavin'
    Address='Ahemdabad'

e1=Company()
e1.name='kanji'
e1.age=22
e1.id=2
e1.mail='kanji@123'

e2=Company()
e2.name='chetan'
e2.age=20
e2.id=3
e2.mail='chetan@213'

print(e1.name,e1.age,e1.id,e1.mail)
# print(e2.name,e2.age,e2.id,e2.mail)

#~ output:-
"""
kanji 22 2 kanji@123
chetan 20 3 chetan@213"""
e1.age=25 # objecl property value update

print(e1.name,e1.age,e1.id,e1.mail)
#~ output:-
"""
kanji 22 2 kanji@123
kanji 25 2 kanji@123
"""





