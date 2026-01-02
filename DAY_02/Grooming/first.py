# def a():
#     def b():
#         nonlocal x
#         print(x,y)
#         x=40
#         print(x+y)
#     x=10
#     y=20
#     b()
# a()

# def demo(*args):
#     print(args)
#     print(type(args))
# demo(5,10,15)
# demo([5,10,15])


# def demo(*args):
#     out=0
#     for i in args:
#         out=out+i
#     return out
    
# print(demo(5,10,15))

# num = 5
# fact = 1
# i=1

# while i<=num:
#     fact = fact * i
#     i+=1


# print("Factorial:", fact)

# def rec(n,i=1):
#     if n<=0:
#         return i
#     i*=n
#     return rec(n-1,i)
# print(rec(int(input("enter number: "))))

n=98251

# i=0
# while i<n:
#     sum=0
#     if i%2==0:
#         sum+=i
#     i+=1
# print(i)


# n=98251

# def sum_off(n,i=0):
#     if i>=n:
#         return i
#     ld=n%10
#     if ld%2==0:
#         n=n//10
#     return sum_off(i+1)
# print(sum_off(n))


#oops in python

class A:
    def __init__(self,A):
        self.A=A
    def __add__(self,other):
        return self.A*other.A

ob1=A(10)
ob2=A(20)
print(ob1+ob2)



