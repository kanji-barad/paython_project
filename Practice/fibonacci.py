
#!using recursion

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=10
for i in range(n+1):
    print(fibo(i))

#! while loop

i=0
n=10
a,b=0,1
while i<=n:
    print(a)
    a,b=b,a+b
    i+=1
    
#! for loop

n=10
a,b=0,1
for i in range(n+1):
    print(a)
    a,b=b,a+b

