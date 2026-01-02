def perfect(n):
    out=0
    for i in range(1,n):
        if n%i==0:
            out=out+i
    if n==out:
        return "perfect number"
    else:
        return "not perfect number"

print(perfect(6))
print(perfect(10))

#!packing and unpacking:-

#packing:-
#.    the finomenon of grouping individual values in the format of collection to keep the values secured.

#!Note:-
#.   our system will bydefault will do packing in the format of tuple
#!Reason:-
# because tuple is the most secured data type.

#there are 2 typpe of packing:-
#!1.tuple/single packing

#val1,val2,val3.....,valn----->*var/*args
#syntax:-
       #def fname(*var/args):
           #statment of block
        #fname(val1,val2,val3,.....,valn)

#example:-
def demo(*args):
    return args

# print(demo(12,21)) #-->(12,21)
# print(demo()) #-->empty tuplpe

#  (*)is responsible for packing (single)
# args is a variable in which the values will be stored in the format of tuple.

def add(*args):
    print(args)
    out=0
    for i in args:
        out=out+i
    return out
print(add(12,24,56))
print(add(12))


#!2.dictionary /double packing:-

#it is a phenomenon of gruping the individual key-value pair in the form of dictionary toprovide security.

#k1=v1,k2,v2....,kn=vn --->**var

def dictionary(**kwargs):
    return (type(kwargs),kwargs)

# print(dictionary(a=10,b=20))
# print(dictionary(name="kanji",age=25))

#!Note:-
     #keys shold follow the rules of iidentifiers.
     #key should be of string datatype only.
     #keys shouldn't enclose with quotes ,but values are stored in the format of dictionary.

#!combination of both:-

def all(*args,**kwargs):
    print(args)
    print(kwargs)

# all(12,32,a='kanji',b='barad') #--->sequence matter first you give only args value than give me kwargs value.

#?output:-
      #(12, 32)
      #{'a': 'kanji', 'b': 'barad'}


#!unpacking:-
           #the phenomenon of dividing the collection and storing each and every value present in the collection to a unique value.

           #(*)collection ------>var1,var2,var3.....,varn

#!Syntax:-
          #def fname(var1,var2,var3....,varn):
            #statment of block
          #fname(*collection)

def unpack(a,b,c):
    print(a)
    print(b)
    print(c)
unpack(*(10,12,13))
# 10
# 12
# 13
unpack(*{'name':'kanji','surname':'barad','age':23})
# name
# surname
# age
unpack(*(12,'hii','byy'))
# 12
# hii
# byy
unpack(*{12,'hii','byy'})
# byy
# 12
# hii

#!Assignment:-



# 1.Find the factorial of a number using for loop

num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)


# 2.wap to print the ascii values of all uppercase characteres

for ch in range(65, 91):   
    print(chr(ch), ":", ch)


# 3.create a list of cube of numbers beetween 1 to 30

cubes = []

for i in range(1, 31):
    cubes.append(i ** 3)

print(cubes)

# 4.sum of integeres from the heterogenius list using for loop

lst = [10, "hello", 5.5, 20, "python", 30]
total = 0

for item in lst:
    if type(item) == int:
        total = total + item

print("Sum of numbers:", total)

# 5.extract all the integeres from the list which are multiple of 5 and is three digit number from list.
lst = [10, 55, 100, 125, 500, 999, 1000, 45, 75]
result = []

for num in lst:
    if num % 5 == 0 and 100 <= num <= 999:
        result.append(num)

print("numbers:", result)