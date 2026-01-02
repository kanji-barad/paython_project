
#!(1). Single/Multiple Argument Pass:-
def greetings(name):
    print(f"hello {name}!")

greetings('kanji')
# greetings().   #give me an error because name is required argument.

#!(2). Default Argumentes:-
def greetings(name='world'):  #?Default Argument
    print(f"hello {name}")

greetings() #?Without given error using Default Argumentes Take 
greetings('kanji') #?Default Argumentes Ignore 


#!(3).Keyword Argumentes:-(named argument):-
def division(a,b):  #? parameteres
    return a/b

result1 = division(100,20) #? positional(sequence) Argument
print(result1)

result2 = division(b=100,a=20) #?Keyword(named) Argument -->sequence not matter
print(result2)


#!(4).Arbitrary Argument:-
#^(1).Arbitrary positional argumentes (*args):-
#*note:- stores argumentes as tuple

def add_sum(*args):
    print(type(args)) #?-->. <class 'tuple'> stores argument as a tuple.
    return sum(args)

sum = add_sum(1,2,3,4) #! variable (n)no of argumentes given
print(sum)

#~example:-2.

def names_print(*names):
    for name in names:
        print(f"Hello {name}!")

names_print('kanji','yuvraj','dinesh','vishal')


#^(2).Arbitrary Keyword Argumenters(**kwargs):-
#*dictionary na form ma store thay che **kwargs.

def print_details(**kwargs):
    print(type(kwargs)) #? type dictionary form store
    for key,value in kwargs.items():
        print(f'{key} : {value}')

print_details(name = 'kanji',age = 23)