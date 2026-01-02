
#!Types Of Argumentes:-

#1.positional argumentes
#2.default argumentes
#3.keyword argumentes
#4.variable length argumentes


#difference between parameters and argumentes:-
# parameters are piresent during function declaration where as the argumentes are passed during function calling(pd)/)(ac).

#!1.positional argumentes:-
#the argumnetes which are created in function declaration are called as positional argument.

#note:-
# it is compulsory to pass the value.
# follow the same order.

#example:-

def demo(a,b):
    print(a,b)
demo(12,24)

# in the above case a and b are positional argumentes.

#!2.default argumentes:-
# the argumentes which are present in the function declaration and if the user does not passed the value it will take the default value.
# but if the user passes the value then it will take that value itself.

# default argumentes should be always followed by positional argumentes.

#example:-

def info(name,mail,contact,alt_contact=None):
    print('name is',name) 
    print('mail is',mail) 
    print('contact is',contact) 
    print('alt_contact is',alt_contact) 

# in the above example name,mail,conatact are positonal argumentes,where as alternate contactes is an default argument.
# case1:- if the user passes the value for default argument.

info('kanji','kanji@123',7984844987,9879336448)

"""output:-
name is kanji
mail is kanji@123
contact is 7984844987
alt_contact is 9879336448"""

#case2:- if the user does not pass the value for default argumentes.

info('kanji','kanji@123',7984844987)

"""""
output:-
name is kanji
mail is kanji@123
contact is 7984844987
alt_contact is None
"""

#!3.keyword argumentes:-
# the argumentes which are present in function calling and we are passing key valu pairs as the values to the argumentes are called as keyword argument.

#example:-

def pack(**d):
    print(type(d))
    print(d)

pack(a=10,b='20',c=30,d=40)

"""" 
output:-
{'a': 10, 'b': '20', 'c': 30, 'd': 40}
"""

#!4. variable length argumentes:-
# the argumentes which are present in the funcation declaration and this argumentes are capable of taking n number of values.

def pack(*t,**d):
    print(type(t))
    print(t)
    print(type(d))
    print(d)

pack(10,20,30,40,a=10,b=20,c=30)

"""""
output:-
<class 'tuple'>
(10, 20, 30, 40)
<class 'dict'>
{'a': 10, 'b': 20, 'c': 30}
"""

# create a function to extract only vowles from the string.

def extract(n,out=' '):
    for i in n:
        if "A"<=i<='Z' or 'a'<=i<='z':
            if i in 'AEIOUaeiou':
                out=out+i
    return out

print(extract('programming'))

#output:- oai

