# a=int(input("Enter a number: "))

# for i in range(2,a+1):
#     for j in range(2,i):
#         if i%j==0:
#             break

#     else:
#         print(i)    
        
#armstrong number print up to n using for loop only:-





# a=int(input("Enter a number: "))    

# for num in range(1,a+1):
#     num1=str(num)
#     p=len(num1)
#     sum=0
#     for j in num1:
#         sum=int(j)**p
#     if sum==num:
#         print(num)

a=int(input("Enter a number: "))    

# for num in range(1,a+1):
#     num1=str(num)
#     p=len(num1)
#     sum=0
#     for j in num1:
#         sum=int(j)**p
#     if sum==num:
#         print(num)


for i in range(1,a+1):
    sum=0
    p=len(str(i))
    for j in str(i):
        sum=sum+int(j)**p
    if sum==i:
        print(i)