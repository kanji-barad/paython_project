
#!pattern programming:-

#?----> * * * *

# n=4 
# for i in range(1,n+1):
#     print("*",end=" ") 
# print()

#?---->
"""""
* * * *
* * * *
* * * *
* * * *
"""
# for i in range(1,4):       
#     for j in range(4):    
#         print("*", end=" ")
#     print()               

#?--->
"""""
* * *
* * *
"""

# for i in range(1,2+1):        
#     for j in range(j+1):    
#         print("*", end="  ")
#     print()


#?--->
"""""
@ 
* @ 
* * @ 
* * * @ 
* * * * @ 
"""
# n = 5

# for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             if i==j:
#                 print("@",end=" ")
#             elif i>j:
#                 print("*",end=" ")
#         print()

#?---->
"""""
* * * * *
  * * * *
    * * *
      * *
        *

"""

# n = 5

# for i in range(1, n+1):
#         for j in range(1, n+1 ):
#             if i==j or i<j:
#                 print("*",end=" ")
#             else:
#                  print(" ",end=" ")
#         print()

            

#?---->
"""""
@ * * * *
* @ * * *
* * @ * *
* * * @ *

"""

# for i in range(4):              
#     for j in range(5):          
#         if i == j :              
#             print("@", end=" ")
#         elif i>j:
#             print("#",end=" ")
#         else:
#             print("*", end=" ")
#     print()


#?---->
"""""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# for i in range(1, 6):          
#     for j in range(i):         
#         print(i, end=" ")
#     print()


#?---->
"""""
1 0 0 0 0
  1 0 0 0
    1 0 0
      1 0
        1
"""

# n = 5

# for i in range(n):
#     for k in range(i):
#         print(" ", end=" ")
#     print("1", end=" ")
#     for j in range(n - i - 1):
#         print("0", end=" ")
#     print()





         
