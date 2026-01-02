
#!1️⃣ Palindrome Number

#Number same forward & reverse

n = int(input("Enter number: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


#🧠 Explanation (Gujarati):
#Number ને reverse કરીએ અને original સાથે compare કરીએ.

#!2️⃣ Prime Number

#Only divisible by 1 & itself

n = int(input("Enter number: "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")


#🧠 Prime number પાસે exactly 2 divisors હોય.

#!3️⃣ Fibonacci Series
n = int(input("Enter terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a+b


#🧠 Next number = previous two numbers sum.

#!4️⃣ Factorial
n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial:", fact)


#🧠 Factorial = 5! → 5×4×3×2×1

#!5️⃣ Reverse Number
n = int(input("Enter number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reverse:", rev)

#!6️⃣ Armstrong Number

#Sum of digits power length = number

n = int(input("Enter number: "))
temp = n
length = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** length
    n //= 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")


#Example: 153 → 1³+5³+3³ = 153

#!7️⃣ Perfect Number

#Sum of divisors = number

n = int(input("Enter number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect")

#!8️⃣ Sum of Digits
n = int(input("Enter number: "))
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print("Sum:", sum)

#!9️⃣ Leap Year
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

#!🔟 GCD & LCM
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# GCD
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x

lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)

#!1️⃣1️⃣ Even / Odd
n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#!1️⃣2️⃣ Count Digits
n = int(input("Enter number: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Digits:", count)

#!1️⃣3️⃣ Greatest of 3 Numbers
a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print("A is greatest")
elif b > c:
    print("B is greatest")
else:
    print("C is greatest")

#!1️⃣4️⃣ ASCII Character Convert
ch = input("Enter character: ")
print("ASCII value:", ord(ch))

num = int(input("Enter ASCII number: "))
print("Character:", chr(num))

#!1️⃣5️⃣ Pattern Printing
n = 5
for i in range(1, n+1):
    print("* " * i)


#Output:
"""
*
* *
* * *
* * * *
* * * * *
"""

#!16.balanced number
num = input("Enter number: ")

length = len(num)
mid = length // 2

# Left part
left = num[:mid]

# Right part
if length % 2 == 0:
    right = num[mid:]
else:
    right = num[mid+1:]

left_sum = 0
right_sum = 0

for i in left:
    left_sum += int(i)

for i in right:
    right_sum += int(i)

if left_sum == right_sum:
    print("Balanced Number")
else:
    print("Not Balanced Number")
