
#~ syntax:-

# def func_name(func):
#     def wrapper(*args,**kwargs):
#         #any logic here
#         return func(*args,**kwargs)
#     return wrapper
# @func_name #~decorater 
# def  sum_two_num(a,b):
#     return a+b
    
    



# def call_counter(func):
#     count=0
#     def wrapper(*args,**kwargs):
#         nonlocal count
#         count+=1
#         print(count)
#         print('funcation call',count,"times")
#         return func(*args,**kwargs)
#     return wrapper

# def greet(name):
#     print("Hello",name)

# greet('dinesh')
# greet('kanji')
# greet('yuvraj')


# def upper_func(func):
#     def wrapper():
#         result=func()
#         return result.upper()
#     return wrapper

# @upper_func
# def message():
#     return ('python is easy')

# print(message())






# def add_func(func):
#     def wrapper(*args,**kwargs):
#         print(func(*args,**kwargs))
#         print("function is called")
        
#     return wrapper

# @add_func
# def addition(a,b):
#     return a + b

# addition(10,20)


#! aa decorater har wakhte function call thay tyare 4 second no time ley che.
import time

def cahe(func):
    cache_value={}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
        
    return wrapper


@cahe
def long_runnung_func(a, b):
    time.sleep(4)
    return a+b

print(long_runnung_func(3,4)) #first 4 second
print(long_runnung_func(1000,500)) #second 4 second


