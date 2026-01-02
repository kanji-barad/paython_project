
#! using for loop
s1=[1,2,3,4,5]
s2=[1,4,5]

common=[]
for i in s1:
    if i  in s2:
        common.append(i)

print(common)

#! using while loop

s1=[1,2,3,4,5]
s2=[1,4,5]

common=[]
i=0
while i<len(s1):
    if s1[i] in s2:
        common.append(s1[i])
    i+=1
print(common)

