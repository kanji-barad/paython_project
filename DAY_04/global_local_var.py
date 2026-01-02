# a =20

# def demo():
#     b=10
#     a=30
#     print(a)
#     print(b)
#     print('hii')
# demo()

# a =20

# def demo():
#     global a #?global var access using global keyword
#     b=10
#     a+=12 #?through an error //cannot access local variable 'a' 
#     print(a)
#     print(b)
#     print('hii')
# demo()
# print(a) #? modification global keyword se hota hai to output 32 a ke value ayengi.

"""
┌───────────────────────────┬───────────────────────────┐
│        GLOBAL VARIABLE    │        LOCAL VARIABLE     │
├───────────────────────────┼───────────────────────────┤
│ Defined outside function  │ Defined inside function   │
│                           │                           │
│ a = 20                    │ def demo():               │
│                           │     b = 10                │
│                           │                           │
│ Accessible everywhere     │ Accessible only in demo() │
│                           │                           │
│ Read inside function ✔    │ Read inside function ✔    │
│                           │                           │
│ Modify inside function ❌ │ Modify inside function ✔   |
│ (needs global keyword)    │                           │
│                           │                           │
│ Lifetime: whole program   │ Lifetime: function call   │
│                           │                           │
│ Example: print(a)         │ Example: print(b)         │
└───────────────────────────┴───────────────────────────┘

"""

# we can acess a global variable inside the local space but if we try to modify the global variable inside the local space it will note allow for modification.

# in order to modify a global variable inside the local space we have to use "global" keyword.
# global variable sabse upar likhna hota hai.

#!local variable:-

# if we try to acess a local variable inside nested function we will be able to access it but if we try to modify a local variavble inside nested function it will through an error.

"""
+--------------------+--------------------+------------------------+
|        ACTION      |     LOCAL SCOPE    |    NESTED FUNCTION     |
+--------------------+--------------------+------------------------+
| Accessing variable |        ✔ YES       |         ✔ YES          |
|                    |                    |                        |
| Modifying variable |        ✔ YES       |         ❌ NO           |
+--------------------+--------------------+------------------------+
"""

# example:-

# a=20
# def demo():
#     b=10
#     def demo2():
#         nonlocal b
#         b=b+10
#         print(b)
#     demo2()
# demo()

#!case1:-

# a=20
# b=12
# def demo():
#     def demo2():
#         print(b)
#     demo2()
# demo()

#12

#!case2:-

# a=20
# b=12
# def demo():
#     def demo2():
#         global b
#         b+=12
#         print(b)
#     demo2()
# demo()
# print(b)

#24
#24

#!case3:-

# a=20
# b=12
# def demo():
#     b=13
#     def demo2():
#         nonlocal b
#         b+=12
#         print(b)
#     demo2()
# demo()
# print(b)

#25
#12

