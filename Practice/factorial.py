
#! using recursion
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

#! using for loop
fact=1
n=int(input("enter number"))
for i in range(1,n+1):
    fact=fact*i
print(fact)

#! using while loop
i=5
fact=1
while i<=n:
    if i == 0:
        break
    fact=fact*i
    i-=1
print(fact)

a=5
def fact(a,i=1):
    if i>a:
        return 1
    return i*fact(a,i+1)
print(fact(a))
