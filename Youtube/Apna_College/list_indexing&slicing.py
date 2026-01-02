# # # a=[10,20,[10,20,30,40,[10,20,[20,10]]],30,40,50]
# # # print(a[2][4][1])


# # """""
# # 1️⃣ Print the first element
# # 2️⃣ Print the last element
# # 3️⃣ Print the 3rd element using positive index
# # 4️⃣ Print the 3rd element from end
# # 5️⃣ Change the value 40 to 45 using index
# # 6️⃣ Add 100 at index position 2
# # 7️⃣ Remove the element at index 5
# # 8️⃣ Print all elements using negative indexing
# # 9️⃣ Find the index of 60
# # 🔟 Replace last element with 999"""

# # # nums = [10, 20, 30, 40, 50, 60, 70, 80]
# # # print(nums[:1])
# # # print(nums[-1:])
# # # print(nums[3:4])
# # # print(nums[-3:-2])
# # # nums[-5] = 45
# # # print(nums)
# # # nums[-6]=100
# # # print(nums)
# # # nums.remove(60)
# # # print(nums)
# # # nums[-1:]
# # # print(nums)
# # # idx=nums.index(50)
# # # print(idx)
# # # nums[-1]=99
# # # print(nums)

# # """""
# # 🔹 Part 2: List Slicing Tasks

# # Using same list:

# # nums = [10, 20, 30, 40, 50, 60, 70, 80]

# # 📝 Tasks:

# # 1️⃣ Print first 4 elements
# # 2️⃣ Print last 3 elements
# # 3️⃣ Print elements from index 2 to 5
# # 4️⃣ Print all elements except first and last
# # 5️⃣ Print alternate elements
# # 6️⃣ Reverse the list using slicing
# # 7️⃣ Print elements in reverse order except last element
# # 8️⃣ Print every 3rd element
# # 9️⃣ Copy the entire list using slicing
# # 🔟 Clear the list using slicing"""

# # # nums = [10, 20, 30, 40, 50, 60, 70, 80]
# # # print(nums[:4])
# # # print(nums[-3:])
# # # print(nums[2:6])
# # # print(nums[::])
# # # print(nums[::2])
# # # print(nums[::-1])
# # # print(nums[-8:])
# # # print(nums[::3])
# # # barad=nums[::]
# # # print(barad)
# # # barad.clear()
# # # print(barad)


# # """""
# # data = [5, 10, 15, 20, 25, 30]
# # 🧠 Tasks:
# # 1️⃣ Print middle element(s)
# # 2️⃣ Split list into two equal parts
# # 3️⃣ Reverse only the first half
# # 4️⃣ Get elements greater than 15 using slicing logic
# # 5️⃣ Swap first and last element using indexing
# # 6️⃣ Remove middle element using index
# # 7️⃣ Print list except first 2 and last 2 elements
# # 8️⃣ Rotate list left by 2 positions
# # 9️⃣ Rotate list right by 1 position
# # 🔟 Check whether list is palindrome using slicing"""

# # data = [5, 10, 15, 20, 25, 30]
# # # print(data[2:4])

# # # # Split list into two equal parts

# # # data1=len(data)//2
# # # part1=data[data1:]
# # # part2=data[:data1]
# # # print(part1)
# # # print(part2)

# # # #3️⃣ Reverse only the first half
# # # print(part2[::-1])

# # # a = [[]] * 3
# # # a[0].append(1)
# # # print(a)

# # # a = [1, 2, 3]
# # # print(a[::-2])

# # # a = [1, 2, 3, 4]
# # # print(a[1:100])

# # # a = [1, 2, 3]
# # # b = a
# # # del b[0]
# # # print(a)

# # # a = [1, 2, 3]
# # # print(a + [4])
# # # print(a)

# # # a = [1, 2, 3,[4,5,6,[7,8,9]]]
# # # # print(a.extend([2]))
# # # print(a[3][3][1])

# # # a=[100,20,30,40, [10,[20,[30,40]]] , [50,[60]] , [70]]
# # # # print(a[5][0])
# # # print(a[-3][-2])
# # # print(a[::-1])
# # # print(a[-3][-1][-1][-1])
# # # print(a[-3][-2])

# # # a=[1,4,8,[9,0,8,[0,[18,9,[20,[22,[25,28]]]]]]]
# # # print(a[-1][-1][-1][-1][-2])

# # # a=['mango','banana']
# # # b=[['kesar','dates']]
# # # a.extend(b)
# # # print(a)

# # # list1=[1,2,3]
# # # list2 =['a','b']

# # # for i in list2:
# # #     list1.append(i)
# # # print(list1)


# # #!list comprehension:-

# # square= [x**2 for x in range(1,6)]
# # print(square)

# # even= [x for x in range(1,11) if x%2==0]
# # print(even)

# # odd=[x for x in range(1,11) if x%2!=0]
# # print(odd)

# # lst=["1",'2','3','4']

# # # for i in lst:
# # #     print(i)
# # l= [int(i) for i in lst]
# # print(l)

# # words = ["python", "java", "c"]

# # length=[len(x) for x in words]
# # print(length)

# # chars = ['a', 'b', 'c']
# # upper_case=[x.upper() for x in chars]
# # print(upper_case)

# # # nums = [1,2,3,4,5,6,7]
# # # for x in nums:
# # #     if x%2!=0:
# # #         print(x)

# # # even=[x for x in nums if x%2!=0]
# # # print(even)

# # # 7️⃣ Get numbers divisible by 3 and 5 (1–100)

# # num=[x for x in range(1,101) if x%3==0 and x%5==0]
# # print(num)

# # words = ["apple", "cat", "banana", "dog"]

# # user=[x for x in words if len(x)>4]
# # print(user)

# # nums = [1,2,3,4,5]

# # even_odd=["even" if x%2==0 else x for x in nums]
# # print(even_odd)

# # nums = [-5, 10, -2, 8]
# # nums1=[0 if 0>n else n for n in nums]
# # print(nums1)

# # empty=[]
# # for n in nums:
# #     if n<0:
# #         empty.append(0)
# #     else:
# #         empty.append(n)
# # print(empty)

    
# # matrix = [[1, 2], [3, 4], [5, 6]]
# # flat=[num for row  in matrix for num in row]
# # print(flat)

# # em=[]
# # for row in matrix:
# #     for num in row:
# #         em.append(num)
# # print(em)
        
# # table= [(1,1),(1,2),(1,3),(2,1)]

# # t=[(i,j,i*j)for i in range(1,11)  for j in range(1,11)]
# # print(t)

# for i in range(1,11):
#     t=[(i,j,i*j) for j in range(1,10)]
#     print(t,end="\n")
# print()

# # 1️⃣3️⃣ Print all pairs where sum > 5
# a = [1,2,3]
# b = [4,5,6]

# result=[(i,j) for i in a for j in b if (i+j)>5]
# print(result)

# s = "programming"
# a="aeiouAEIOU"
# vowles="".join([i for i in s if i not in a ])
# print(vowles)

# s = "a1b2c3"

# res=[ch for ch in s if ch.isdigit()]
# res1=[ch for ch in s if ch.isalpha()]
# print(res)
# print(res1)

# words = ["python", "java"]

# # res2= [ch[::-1] for ch in words ]
# # print(res2)


# # 1️⃣8️⃣ Get common elements between two lists

# a = [1,2,3,4]
# b = [3,4,5,6]
# c=a+b

# empty=[]
# # 1.way:-
# empty=list(set(c))
# print(empty)

# # 2.way:-
# [empty.append(i) for i in c if i not in empty]
# print(empty)


# for i in c:
#     if i not in empty:
#         empty.append(i)
# print(empty)


# l=[1,2,3]
# l1=[3,4,5]

# r=[(i,j) for i in l for j in l1 if i==j]
# print(r)

#1️⃣9️⃣ Generate prime numbers (1–50)

# primes=[n for n in range(2,51) if all(n%i!=0 for i in range(2,int(n**0.5)+1))]
# print(primes)

# 2️⃣0️⃣ Replace numbers:

# Even → "E"

# Odd → "O"

# nums = [1,2,3,4,5]

# replace=["E" if i%2==0 else "O" for i in nums]
# print(replace)

# for i in nums:
#     if i%2==0:
#         print("e")
#     else:
#         print("o")


# 🔥 CHALLENGE TASK
# 2️⃣1️⃣ Create this pattern using list comprehension
# *
# * *
# * * *
# * * * *

# res=[("*"*i)for i in range(1,5)]
# for j in res:
#     print(j)

# a = [[] for _ in range(3)]
# print(a)

# lst=[10,20,30,40,50]
# k=2
# result=lst[k:]+lst[:k]
# print("left side:",result)

# lst1=[20,40,60,80,100]
# j=3
# result1=lst1[-j:]+lst1[:-j]
# print("right side:",result1)

# lst = [12, 35, 1, 10, 34, 1]
# largest = second = float("-inf")

# for num in lst:
#     if num > largest:
#         if num >largest:
#             second=largest
#             largest=num
#     elif num > second and num != largest:
#         second =num
# print(largest)
# print(second)

# lst = [1, 2, 3, 4, 5]

# flag = True

# for i in range(1,len(lst)):
#     if lst[i]<=lst[i-1]:
#         flag=False
#         break
# print(flag)



# lst = [1, 2, 2, 3]
# flag=True

# for i in range(1,len(lst)):
#     if lst[i]<=lst[i-1]:
#         flag=False
#         break
# print(flag)

# 7️⃣ Remove duplicates but keep order

# Input:

# lst = [1, 2, 2, 3, 1, 4]


# Output:

# [1, 2, 3, 4]

# lst = [1, 2, 2, 3, 1, 4]
# empty=[]
# for i in lst:
#     if i not in empty:
#         empty.append(i)
# print(empty)

# 8️⃣ Remove duplicates (string list)

# Input:

# lst = ["a", "b", "a", "c", "b"]


# Output:

# ["a", "b", "c"]

# lst = ["a", "b", "a", "c", "b"]

# empty=[]

# for i in lst:
#     if i not in empty:
#         empty.append(i)
# print(empty)

# 🔹 List Comprehension (Interview Level)
# nums = [10, -5, 0, 20, -3]

# nums=[10,-5,0,20,-3]
# empty=[]
# for i in nums:
#     if i<0:
#         empty.append(0)
#     else:
#         empty.append(i)

# print(empty)


# 1️⃣ Replace negative → 0, zero → 1

# Input:

# [10, -5, 0, 20, -3]


# Output:

# [10, 0, 1, 20, 0]

# num=[10,-5,0,20,-3]

# empty=[]
# for i in num:
#     if i<0:
#         empty.append(0)
#     elif i==0:
#         empty.append(1)
#     else:
#         empty.append(i)
# print(empty)

# 2️⃣ Create dictionary {num: square}

# Input:

# [10, -5, 0, 20, -3]


# Output:

# {10: 100, -5: 25, 0: 0, 20: 400, -3: 9}

# num=[10,-5,0,20,-3]

# empty={}
# for i in num:
#     empty[i]=i*i
# print(empty)

# 3️⃣ Find missing number from range

# Input:

# lst = [1, 2, 3, 5]
# range = 1 to 5


# Output:

# 4

# lst = [1, 2, 3, 5]

# range1=range(1,6)
# for i in range1:
#     if i not in lst:
#         print(i)

# 4️⃣ Find missing number

# Input:

# lst = [0, 1, 3, 4]
# range = 0 to 4


# Output:

# 2

# lst = [0, 1, 3, 4]
# range1=range(4)

# for i in range1:
#     if i not in lst:
#         print(i)

# 5️⃣ Count frequency using comprehension

# Input:

# lst = [1, 2, 2, 3, 3, 3]


# Output:

# {1: 1, 2: 2, 3: 3}

# freq = {}
# lst = [1, 2, 2, 3, 3, 3]

# for x in lst:
#     freq[x] = freq.get(x, 0) + 1
# print(freq)

# my_list=["apple",'mango','cherry']

# uppercase_list=[lst.upper() for lst in my_list]
# print(uppercase_list)

# nested_list=[[1,2],[3,4],[5,6]]

# # result =[j for i in nested_list for j in i]
# # print(result)

# def sub_list(lst):
#     return [j for i in lst for j in i]
# res=sub_list(nested_list)
# print(res)