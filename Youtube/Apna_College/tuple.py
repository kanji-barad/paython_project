# t=(10,20)
# a,b=t
# print(a)
# print(b)

# lst = [(1, 2), (3, 4)]
# lst[0] = (5, 6)
# print(lst)

# t = (1, [2, 3])
# t[1].append(4)
# print(t)

# t = (5, 1, 4)
# print(tuple(sorted(t)))

# t = tuple(x*x for x in range(5))
# print(t)

# t = (1, 2, 3, 2, 1)
# print(t==t[::-1])

# t = ((1,2), (3,4))
# print(sum(t, ()))

# t = [(1,2), (5,1), (3,4)]
# print(max(t, key=sum))

# t=(1,2,(3,(4)))
# print(t[2][1])

# t=(1,2,(3,4),5,6,(7,9,(9,10)))
# print(t[5][1])
# print(t[5][2][0])

# t=(1,2,(3,4,(5,(6,7,(8,(9,(10)))))))
# print(t[2][2][1][2][1][1])

# t=((1,2),(3,4),(5,6))

# r=[j for i in t for j in i]
# rs=tuple(r)
# print(rs)
# print(type(rs))

# 2️⃣0️⃣ Common Elements

# Find common elements between two tuples

# Output must be tuple

# t=(1,2,3)
# t2=(3,4,5)

# r=tuple(i for i in t if i in t2)
# print(r)


# n=11
# if (n//2)*2==n:
#     print("even")
# else:
#     print("odd")

# n=11
# if n%2==0:
#     print("even")
# else:
#     print("odd")

tuple1=(1,2,3)
tuple2=('a','b','c')
tup3={}

# for i in range(len(tuple1)):
#     tup3[tuple1[i]]=tuple2[i]
# print(tup3)
    
# tuple1 = (1,2,3)
# tuple2 = ('a','b','c')

# result = {tuple1[i]: tuple2[i] for i in range(len(tuple1))}
# print(result)

# res={tuple1[i]:tuple2[i] for i in range(len(tuple2))}
# print(res)

for i in range(len(tuple2)):
    tup3[tuple1[i]]=tuple2[i]
print(tup3)

tup=('kanji','kanji')
print(tup.count('kanji'))

#pacing and unpackin in tuple
a='kanji'
b=21
c='devloper'

barad=a,b,c
print(barad)

name,age,work=barad
print(name)
print(age)
print(work)

