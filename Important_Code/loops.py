
#! 1. S1= PyTHONNative
# O/p=yativePTHONN



# s = "PyTHONNative"
# l = ""
# u = ""
# for i in s:
#     if i == i.lower():
#         u+=i
#     else:
#         l+=i

# print(u+l)

#!2. s2=’PyTHon’
#  output=’PTHyon’

# s2='PyTHon'
# up=""
# lo=""

# for i in s2:
#     if 'A'<=i<='Z':
#         up+=i
#     else:
#         lo+=i
# res=up+lo
# print(res)


#! 3.string="P@#yn26at^&i5v”
# Chars=8
# Digits=3
# Symbol = 4



# string = "P@#yn26at^&i5v”"
# char=0
# digit=0
# symbol=0
# for i in string:
#     if 'a'<=i<='z' or 'A'<=i<='Z':
#         char+=1
#     elif '0'<=i<='9':
#         digit+=1
#     else:
#         symbol+=1
# print(char)
# print(digit)
# print(symbol)



# #! 4. Input - ‘my name is yash patel’
# # Output- ‘**patel yash is name my**’

# s = "my name is yash patel"

# l = s.split()

# res = "**"

# for i in range(len(l)-1,-1,-1):
#     res=res+l[i]+" "
# res=res.strip()+"**"
# print(res)


#! 4. Write a program to remove duplicates from the list

# l=[1,1,2,2,3,4,5]
# res=[]

# for i in l:
#     if i not in res:
#         res.append(i)
 
# print(res)

#!5. Write a program to find largest/second largest number from the list

# l = [10, 25, 5, 40, 30]

# largest = l[0]
# second_largest = l[0]

# for i in range(1, len(l)):
#     if l[i] > largest:
#         second_largest = largest
#         largest = l[i]
#     elif l[i] > second_largest and l[i] != largest:
#         second_largest = l[i]

# print("Largest:", largest)
# print("Second Largest:", second_largest)


#!6. s=[10,20,30,25,35,40]
# b=[10,35,40]
# output=[20,30,25]


# s = [10,20,30,25,35,40]
# b = [10,35,40]

# result = []

# for i in range(len(s)):
#     found = False

#     for j in range(len(b)):
#         if s[i] == b[j]:
#             found = True
#             break


#     if found != False:
#         result.append(s[i])

# print(result)

#!7. l=[’S1001’,’S1002’,’S1003’,’S1004’]
# h=[’Virat’,’Rohit’,’Black’,’Jhon’] 
# b=[34,33,80,60] 
# output=[{’S1001’:{’Virat’:34}},{’S1002’:{’Rohit’:33}},{’S1003’: {’Black’:80}},{’S1004’:{’Jhon’:’60’}}]

# l=['S1001','S1002','S1003','S1004']
# h=['Virat','Rohit','Black','Jhon'] 
# b=[34,33,80,60] 

# result=[]

# for i in range(len(l)):
#     temp={}
#     inner={}

#     inner[h[i]]=b[i]
#     temp[l[i]]=inner

#     result.append(temp)
# print(result)
    
#!8. D = ['red','black','yellow']
# Output = ['c','red','c','black','c','yellow']

# D = ['red','black','yellow']
# result=[]

# for i in range(len(D)):
#     result.append('c')
#     result.append(D[i])
# print(result)
    
#!9. a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23]
# output=[2,3,5,7,11,13,17,23]
#  using advance concepts


# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23]

# primes = [n for n in a if n > 1 and all(n % i != 0 for i in range(2, n))]

# print(primes)

#!10. Write a python program to count how many numbers are greater than 50 and count how many numbers are odd numbers.
# Input list: [10, 55, 42, 17, 58] Output: Numbers greater than 50 : 2 Odd numbers : 3

# l1=[10, 55, 42, 17, 58]

# count=0

# for i in l1:
#     if i>50:
#        count+=1
#     elif i%2!=0:
#         count+=1
#         print("odd numbers: ",count)


# print("50:",count)

#!11. Write a python program to find the highest marks and how many students got them.
# Input: marks = {'Anu': 85, 'Raj': 90, 'Meena': 92, 'Kiran': 92}
# Output:
# Highest Marks : 92 Students : ['Meena', 'Kiran']

# marks = {'Anu': 85, 'Raj': 90, 'Meena': 92, 'Kiran': 92}
# higest=0
# for key,values in marks.items():
#     if marks[key]> higest:
#         higest=marks[key]
    
# name=[]
# for key,values in marks.items():
#     if marks[key]==higest:
#         name.append(key)
# print("higest marks is",higest)
# print("name",name)


        