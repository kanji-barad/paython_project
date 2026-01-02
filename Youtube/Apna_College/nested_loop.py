# for j in range(3):
#     for i in range(1,4):
#         print(i)
#     print()

# i =1
# while i<4:
#     for j in range(1,4):
#         print(j)
#     i+=1
#     print("----------")
    
"""""
1 1 1
2 2 2
3 3 3"""

# i=1
# while i<4:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()
#     i+=1
#     print("----")    


"""""
*
* *
* * *
* * * *"""

# i=1
# while i<5:
#     for j in range(i):
      
#         print("*",end=" ")
#     print()
#     i+=1
    
# for i in range(1,8):
#     print("i is :",i)
#     for j in range(2,i):
#         print("j is: ",j)
#         if i%j==0:
#             break
#     else:
#         print(i)

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


"""""
    *
   **
  ***
 ****
*****
"""

# n = 5
# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print(" ", end="")
#     for star in range(i):
#         print("*", end="")
#     print()

# my_string="barad kanji"
# vowels="aeiou"
# count=0

# for char in my_string:
#     if char.lower() in vowels:
#         count+=1
# print(count)

# my_str="pyton by kanji barad"
# empty=""
# wordes=my_str.split()

# for word in wordes:
#     if len(word)>len(empty):
#         empty=word
# print(empty)

# while True:
#     usr=int(input("enter number greter than 10: "))

#     if usr>10:
#         print(f"you entered {usr}")
#         break