
#! using for loop
s=[1,2,2,3,4,4,5]
d=[]
for i in s:
    if i not in d:
        d.append(i)
print(d)


#! using while loop

s=[1,2,2,3,4,4,5]
d=[]
i=0
while i<len(s):
    if s[i] not in d:
        d.append(s[i])
    i+=1
print(d)

