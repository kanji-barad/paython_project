# wap to creat function to find factorial of a given number

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))


#! steps to convert the looping program in the form of recursion:-

#initialisation of all the required variables of looping should be done in function declaration.
#the termination condition should be written exactly opposite to the looping condition in the form of if statment.
#return the total result inside the termination condition.
#logic of program should be written as it is.
#updation of looping variable should be done in recursive call.
# > ==> <=
# < ==> >=

#while loop:

# n=int(input("enter number: "))
# out=1
# while n>0:
#     out=out*n
#     n=n-1
# print(out)
"""
   Sign        Opp
---------------------
    >     |     <
    <     |     >
   <=     |     >=
   >=     |     <=
   ==     |     !=
   !=     |     ==
"""

# def fact(n,out=1):
#     if n<=0:
#         return out
#     return fact(n-1,out*n)

# print(fact(5))


# #wap to print only even numbers from 1 to 20



# # i=2
# # while i<=20:
# #     if i%2==0:
# #         print(i)
# #     i+=1

# #without return statment:-
# def even(n,i=2):
#     if i>20:
#         return 
#     if i%2==0:
#         print(i)
#     even(n,i+1)
# even(20)

#caf to print fibonacci number using recursion

        
# Fibonacci using while loop

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1
# i = 0

# while i < n:
#     print(a)
#     a,b=b,a+b
#     i += 1






def fibonacci(a, b, n):
    if n == 0:          
        return
    print(a)
    fibonacci(b, a + b, n - 1)

n = int(input("Enter number of terms: "))
fibonacci(0, 1, n)




        


















