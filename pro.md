7. l=[’S1001’,’S1002’,’S1003’,’S1004’]
h=[’Virat’,’Rohit’,’Black’,’Jhon’] b=[34,33,80,60] output=[{’S1001’:{’Virat’:34}},{’S1002’:{’Rohit’:33}},{’S1003’: {’Black’:80}},{’S1004’:{’Jhon’:’60’}}]

nput: marks = {'Anu': 85, 'Raj': 90, 'Meena': 92, 'Kiran': 92}
Output:
Highest Marks : 92 Students : ['Meena', 'Kiran']

14.Write a python program to remove the duplicates from the list and add the non-duplicate values to the second list.
Input:
L1 = [1, 3, 1, 5, 2, 1, 4, 5, 6, 6, 2, 7]
Output:
L2 = [1, 2, 3, 4, 5, 6, 7]

18. s=aaabbccddd
  output=a3b2c2d3


19. What is the output of the following code
  a=24
  b=12
  c=0
  d= a or c
  e=d and b
  print(d+e)



20. Write a program to check whether the given list is a sublist or not

22.Validate pin it must have 4 digits it should not have 3 continuous numbers eg.123 one digit should not repeat 3 times eg. 333

25. Extract and count the highest number of char from string

26. list=[1,0,1,0,1,0,1,0]
Output will be = [0,0,0,0,1,1,1,1]



pattern programming:-

⭐ Pattern 1: Square Pattern
* * * *
* * * *
* * * *
* * * *

for i in range(4):
    print("* * * *")

⭐ Pattern 2: Right Angle Triangle
*
* *
* * *
* * * *

for i in range(1, 5):
    print("* " * i)

⭐ Pattern 3: Reverse Right Angle Triangle
* * * *
* * *
* *
*

for i in range(4, 0, -1):
    print("* " * i)

⭐ Pattern 4: Number Pattern
1
1 2
1 2 3
1 2 3 4

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

⭐ Pattern 5: Same Number Pattern
1
2 2
3 3 3
4 4 4 4

for i in range(1, 5):
    print((str(i) + " ") * i)

⭐ Pattern 6: Alphabet Pattern
A
A B
A B C
A B C D

for i in range(1, 5):
    for j in range(i):
        print(chr(64 + j), end=" ")
    print()

⭐ Pattern 7: Pyramid Star Pattern
   *
  * *
 * * *
* * * *

for i in range(1, 5):
    print(" " * (4 - i) + "* " * i)

⭐ Pattern 8: Simple 0-1 Pattern
1
0 1
1 0 1
0 1 0 1

for i in range(1, 5):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()

⭐ Pattern 9: Hollow Square
* * * *
*     *
*     *
* * * *

for i in range(4):
    if i == 0 or i == 3:
        print("* * * *")
    else:
        print("*     *")

⭐ Pattern 10: Simple Increasing Numbers
1
2 3
4 5 6
7 8 9 10

num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()