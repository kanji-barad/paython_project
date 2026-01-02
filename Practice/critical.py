#input='aaabbcacddad@123'
#output:-a5b2c2d3

# a='aaabbcacddad@123'
# empty=''


# for i in a:
#     if 'a'<=i<='z':
#         if i not in empty:
#             count=a.count(i)
#             empty+=i+str(count)

# print(empty)
        

#! count vowles:-

# s='kanji@123'
# voeles='aeiouAEIOU'
# count=0
# char=''
# for i in s:
#     if i  in voeles:
#         char=char+i
#         count+=1
# print(count)
# print(char)

#! Count consonants

# s='kanji@123'
# voeles='aeiouAEIOU'
# count=0
# char=''
# for i in s:
#     if i  not in voeles:
#         char=char+i
#         count+=1
# print(count)
# print(char)

#! Character occurrence

# s='programming by'
# empty=''
# count=0
# for i in s:
#     if i not in empty:
#         count=s.count(i)
#         empty=empty+i+str(count)
# print(empty)

#! second method:
# s='my name is barad kanji'
# strip1=s.strip()
# empty={}
# for i in strip1:
#     if i in empty:
#         empty[i]+=1
#     else:
#         empty[i]=1
# print(empty)
       
#! word occurence in sentance:-

# s = "my name is yash my name is python"
# words = s.split()
# result = ""

# for i in words:
#     if i not in result:
#         count=s.count(i)
#         result=result+i+str(count)+" "
# print(result)

#! remove spaces:-
# s='my name is barad kanji'
# result=s.replace(" ",'')
# print(result)

#! replace character:-
# s='my name is barad kanji'
# result=s.replace('my','your')
# print(result)

#! ASCII to char & char to ASCII

# a='kanji'
# for i in a:
#     print(i,ord(i))



# b=[66,120,89,105]
# for i in range(len(b)):
#     print(b[i],chr(b[i]))

# #? 7. l=[’S1001’,’S1002’,’S1003’,’S1004’]
# # h=[’Virat’,’Rohit’,’Black’,’Jhon’] b=[34,33,80,60] 
# # output=[{’S1001’:{’Virat’:34}},{’S1002’:{’Rohit’:33}},{’S1003’: {’Black’:80}},{’S1004’:{’Jhon’:’60’}}]

# l=['S1001','S1002','S1003','S1004']
# h=['Virat','Rohit','Black','Jhon']
# b=[34,33,80,60] 
# empty=[]
# num=1001

# for i in range(len(l)):
#     d={}
#     inner={}
#     inner[h[i]]=b[i]
#     d['S'+str(num)]=inner
#     empty.append(d)
#     num+=1

# print(empty)



#? input: marks = {'Anu': 85, 'Raj': 90, 'Meena': 92, 'Kiran': 92}
# Output:
# Highest Marks : 92 Students : ['Meena', 'Kiran']

# marks = {'Anu': 85, 'Raj': 90, 'Meena': 92, 'Kiran': 92}
# grade=0
# name=[]


# for key,val in marks.items():
#     if val > grade:
#         grade=val
    
# for key,val in marks.items():
#     if val==grade:
#         name.append(key)
       
# print(grade)
# print(name)
    
#! 
# 14.Write a python program to remove the duplicates from the list and add the non-duplicate values to the second list.
# Input:
# L1 = [1, 3, 1, 5, 2, 1, 4, 5, 6, 6, 2, 7]
# Output:
# L2 = [1, 2, 3, 4, 5, 6, 7]
    
# L1 = [1, 3, 1, 5, 2, 1, 4, 5, 6, 6, 2, 7]

# L2=[]

# for i in L1:
#     if i not in L2:
#         L2.append(i)
# print(sorted(L2))

#! 18. s=aaabbccddd
#   output=a3b2c2d3

# s='aaabbccddd'
# empty=''

# for i in s:
#     if 'a'<=i<='z':
#         if i not in empty:
#             count=s.count(i)
#             empty=empty+i+str(count)
# print(empty)

# a=24
# b=12
# c=0
# d= a or c
# e=d and b
# print(d+e)


#! check sublist or not
# a=[1,2,3,4]
# b=[5,6]

# flag=True

# for i in b:
#     if i not in a:
#         flag=False
#         break
# if flag:
#     print('sublist')
# else:
#     print('not a sublist')

# for i in range(1,4):
#     print('* * * *')

# for i in range(1,5):
#     for j in range(i):
#         print('*',end=" ")
#     print()

# print()
# for i in range(4,0,-1):
#     print('*'*i)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

for i in range(1,5):
    print((str(i)+" ")*i)

for i in range(1,5):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

# for i in range(1,5):
#     print(" "*(4-i)+"* "*i)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print((i+j)%2,end=" ")
#     print()

# for i in range(4):
#     if i==0 or i==3:
#         print("* * * *")
#     else:
#         print("*     *")

# num=1

# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

list1=[1,0,1,0,1,0,1,0]
# Output will be = [0,0,0,0,1,1,1,1]

# list2=[]

# count=0
# cout1=0

# for i in list1:
#     if i == 0:
#         count+=1
#     else:
#         cout1+=1
# for j in range(count):
#     list2.append(0)

# for c in range(cout1):
#     list2.append(1)
# print(list2)



    