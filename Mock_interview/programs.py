""""
Task 1

User પાસેથી string લો અને:

length શોધો

reverse કરો
"""

# n=input("enter")

# reverse=""
# for ch in n:
#     reverse=ch+reverse
# print(reverse)


""""
Task 2

String માંથી:

vowels કેટલા છે તે ગણો
"""
# n='programming'

# vowles='AEIOUaeiou'
# count=0
# for ch in n:
#     if ch in vowles:
#         count+=1
# print(count)

"""
Task 4

List માંથી:

maximum value

minimum value શોધો
"""

# l1 = [2,5,3,4,8,10]

# max_val=l1[0]

# for i in l1:
#     if i>max_val:
#         max_val=i
# print(max_val)

# min_val=l1[0]

# for i in l1:
#     if min_val>i:
#         min_val=i
# print(min_val)

#combine:-

# l1 = [2,5,3,4,8,10]

# max_val=l1[0]
# min_val=l1[0]

# for i in l1:
#     if i > max_val:
#         max_val=i
#     if i < min_val:
#         min_val=i
# print(max_val)
# print(min_val)

""""
List માંથી:

even numbers ની નવી list બનાવો
"""

# l2=[1,2,3,4,5,6,7,8,9,10]

# even_list=[]

# for i in l2:
#     if i%2==0:
#         even_list.append(i)

# print(even_list)

""""
Student dictionary બનાવો અને:

name, marks print કરો

marks >= 35 તો Pass else Fail
"""

# student={
#     "Kanji": 45,
#     "Amit": 32,
#     "Ravi": 67,
#     "Neha": 28
# }

# for name in student:
#     marks=student[name]
    
#     if marks>33:
#         print(name ,":",marks, 'Pass')
#     else:
#         print(name ,":",marks, 'Fail')


""""
Task 9

Number positive, negative કે zero છે તે ચેક કરો
"""

# n =10
# if n ==0:
#     print("zero")
# elif n >=1:
#     print("positive")
# elif n<0:
#     print('negative')

""""
Given list માંથી:

sum of elements find કરો
"""

# l3=[1,2,3,4,5]

# sum=0
# for i in l3:
#     sum+=i
# print(sum)

""""
Multiplication table (1 to 10) print કરો
"""
# n=10
# for i in range(1,n+1):
#     print(n, 'X',i ,"=", n*i)

"""
#! Pattern print કરો

*
* *
* * *

"""

# for i in range(1,4):
#     for j in range(i):
#         print("*",end=" ")
#     print()


""""
Number pattern

1
1 2
1 2 3
"""

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

""""
1 થી 10 numbers print કરો using while
"""

# i=1
# while i<=10:
#     print(i)
#     i+=1

"""
Reverse number print કરો
"""
# num=123
# rev=0

# for i in range(len(str(num))):
#     ld=num%10
#     print(ld)
#     rev=rev*10+ld
#     print(rev)
#     num=num//10
#     print(num)
# print(rev)

"""
Function બનાવો:

number even કે odd check કરે
"""

# def num_check(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# print(num_check(5))

"""
Function બનાવો:

two numbers માંથી greater number return કરે
"""

# def greter(a,b):
#     if a>b:
#         return 'a is greter'
#     else:
#         return 'b is greter'
    
# print(greter(20,10))

"""
Function બનાવો:

list pass કરો અને sum return કરો
"""
# l1=[1,2,3,4,5]
# def sum_list(l1):
#     sum=0
#     for ch in l1:
#         sum=sum+ch
#     return sum
# print(sum_list(l1))

"""
Function બનાવો:

1 થી n સુધી numbers print કરે (for loop)
"""

# def number(n):
#     for i in range(1,n+1):
#         print(i) 

# number(10)

"""
Function બનાવો:

list માં કેટલા even numbers છે તે count કરે
"""

# l2=[1,2,3,4,5,6,7,8,9,10]


# def even_count(l2):
#     count=0
#     for i in l2:
#         if i%2==0:
#             count+=1
#     return count
# print(even_count(l2))

"""
Function બનાવો:

string reverse return કરે (for loop)
"""

# s='kanji'
# def rev_l(s):
#     rev=''
#     for i in s:
#         rev=i+rev
        
#     return rev

# print(rev_l(s))

"""
Recursive function:

1 થી n સુધી sum કાઢે
"""

# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n-1)
# print(sum_n(5))

"""
Recursive function:

factorial કાઢે
"""

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))



"""
Recursive function:

number reverse કરે
"""

# def num_reverse(n,rev=0):
#     if n ==0:
#         return rev
#     return num_reverse(n//10,rev*10+n%10)
# print(num_reverse(123))

"""
Recursive function:

Fibonacci series generate કરે
"""

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)

# for i in range(10):
#     print(fibonacci(i),end=" ")
# print()

"""
Factorial:

for loop થી

recursion થી
"""
# for loop:-

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# factorial(5)

#recursion

# def factorial(n):
#     if n==0 or  n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

"""
Function બનાવો:

list લો

even numbers return કરો

recursion use કરો
"""

#even number using function

l1=[1,2,3,4,5,6,7,8,9,10]

# def even_func(l1):
#     for i in l1:
#         if i%2==0:
#             return 'even'

# print(even_func(l1))

# def even_numbers(lst):
#     if lst == []:          # base condition
#         return []

#     if lst[0] % 2 == 0:    # check first element
#         return [lst[0]] + even_numbers(lst[1:])
#     else:
#         return even_numbers(lst[1:])


# print(even_numbers([1, 2, 3, 4, 5, 6]))

#!---------------------Normal Practice--------------------------------

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))


#! fibonacci series method
# f0=0
# f1=1
# f2=f1+f0
# f(n)=f(n-1)+f(n-2)

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(20))

# def show(n):
#     if n == 0:
#         return
#     print(n)
#     return show(n-1)
# show(5)

    
# def sum_no(n):
#     if n==0 or n==1:
#         return 1
#     return sum_no(n-1)+n
# print(sum_no(10))

# l1=[1,2,3,4,5]

# def list_show(l1,idx=0):
#     if idx == len(l1):
#         return
#     print(l1[idx])
#     return list_show(l1,idx+1)
# list_show(l1)

#!Example 4: Even numbers return કરો (Recursion + Function)

# def even_num(list,idx=1,result=[]):
#     if idx==len(list):
#         return result
#     if list[idx]%2!=0:
#         result.append(idx)
#     return even_num(list,idx+1,result)

# list_e=[1,2,3,4,5,6,7,8,9,10]
# print(even_num(list_e))

#! 1 થી n સુધી numbers print કરો

# def show(n):
#     if n==0:
#         return
#     show(n-1)
#     print(n)
# show(5)

# def show(n):
#     if n==0:
#         return
#     print(n)
#     return show(n-1)
# show(5)

#! Factorial of a number

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return factorial(n-1)*n

# print(factorial(5))