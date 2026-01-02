
#!using for loop
s="programminga"
vowles='aeiouAEIOU'
count=0
for i in s:
    if i in vowles:
        count+=1
        print(i)
print(count)

#! using while loop

s="programminga"
vowles="aeiouAEIOU"
count=0
i=0
while i < len(s):
    if s[i] in vowles:
        count+=1
        print(s[i])
    i+=1
print(count)
    