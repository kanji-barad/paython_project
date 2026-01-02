
#! Recursion In Python:-

#recursion:-

# the phenomenon of calling the function by itself until the termination condition becomes True.

#!Syntax:-

#?without return value:-

# def fname(args):
#     if termination-condition:
#         return
#     ----
#     ----
#     ----
#     fname(args)
# fname(values)

#?with return value:-

# def fname(args):
#     if termination-condition:
#         return Value
#     ----
#     ----
#     ----
#     return fname(args)
# print(fname(values))

#! Note:-
# return keyword is used to stop the execution of the function.if it is having any result in front of it, it will display that or else it will just simply terminate the function. 

#^ factorial recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))

