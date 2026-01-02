
#! Q1. using for loop intersection return from 2 lists:-


# lst1=[1,2,4,5]
# lst2=[4,5,6,7,8]

# def inter_section(lst1,lst2):
#     empty=[]
#     for i in lst2:
#         if i in lst1 and i not in empty:
#             empty.append(i)
#     return empty
# print(inter_section(lst1,lst2))

#using list comprehension:-

# def inter_comp(lst1,lst2):
#     return [i for i in lst1 if i in lst2]

# print(inter_comp(lst1,lst2))

#! Q2. find the most frequent element in a list?

# numbers=[1,2,2,3,3,3,4]

# def most_freq(numbers):
#     max_count=0
#     max_freq=None
#     for item in numbers:
#         count=numbers.count(item)
#         if count>max_count:
#             max_count=count
#             max_freq=item
#     return max_freq

# print(most_freq(numbers))

#! Q3. find the sum of givin list:-

# lst=[1,2,3,4,5]
# sum=0
# for i in lst:
#     sum+=i
# print(sum)

# data = {'a': {'b': {'c': 42}, 'd': 7}, 'e': 10}

#output:-{'a.b.c': 42, 'a.d': 7, 'e': 10}
#e:10
#

# def flatten_dict(data,paren_key='',sep="."):
#     empty={}
#     for key,value in data.items():
#         new_key= f"{paren_key}{sep}{key}" if paren_key else key

#         if isinstance(value,dict):
#             empty.update(flatten_dict(value,new_key,sep))
#         else:
#             empty[new_key]=value
#     return empty

# print(flatten_dict(data))

#! Q4. sorted list by values basis using sorted() function:-

# data={'d':5,'b':9,'c':2,'a':7}

# def sort_val(data):
#     sorted_items=sorted(data.items(),key=lambda item:item[1],reverse=True)
#     return {key:value for key,value in sorted_items}
# print(sort_val(data))


#!dictionary creat using dict comprehension:-

# dis={dict:dict for dict in range(1,10)}
# print(dis)

# dic2={key:[val for val in range(5,11)] for key in range(1,6)}
# print(dic2)


