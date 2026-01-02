
#!1️⃣ Palindrome Number
#Check if a number reads the same forward and backward.

num = int(input("Enter number: "))
temp = num
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#!2️⃣ Prime Number
#Check if a number is prime.

num = int(input("Enter number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#!3️⃣ Fibonacci Sequence
#Print Fibonacci numbers up to n.

n = int(input("Enter how many terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#!4️⃣ Factorial
#Calculate factorial of a number.

num = int(input("Enter number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)

#!5️⃣ Reverse Number
#Reverse the digits of a number.

num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed:", rev)

#!6️⃣ Armstrong Number
#Check if number = sum of its digits raised to power of digits count.

num = int(input("Enter number: "))
temp = num
sum = 0
digits = len(str(num))

while temp > 0:
    sum += (temp % 10) ** digits
    temp //= 10

if num == sum:
    print("Armstrong")
else:
    print("Not Armstrong")

#!7️⃣ Perfect Number
#Check if number = sum of its proper divisors.

num = int(input("Enter number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect number")
else:
    print("Not Perfect number")

#!8️⃣ Sum of Digits

num = int(input("Enter number: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("Sum of digits:", sum)

#!9️⃣ Leap Year Check

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

#!🔟 GCD / LCM

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x
print("GCD:", gcd)

# LCM
lcm = (a * b) // gcd
print("LCM:", lcm)

#!1️⃣1️⃣ Even / Odd

num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#!1️⃣2️⃣ Count Digits

num = int(input("Enter number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)

#!1️⃣3️⃣ Greatest of 3 Numbers

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
if a > b and a > c:
    print("Greatest:", a)
elif b > c:
    print("Greatest:", b)
else:
    print("Greatest:", c)

#!1️⃣4️⃣ ASCII Character Convert

ch = input("Enter character: ")
print("ASCII code:", ord(ch))

num = int(input("Enter ASCII code: "))
print("Character:", chr(num))

#!1️⃣5️⃣ Pattern Printing (Simple)
#Example: Triangle pattern

n = int(input("Enter number of rows: "))
for i in range(1, n+1):
    print("* " * i)