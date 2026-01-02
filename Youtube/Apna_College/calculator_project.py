
#!Create A Calculator Using Basic Of Functions:-

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def avg(num1,num2):
    return (num1 + num2)/2

print(f"select operations: \n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Average")

select = int(input("Enter your operation here 1,2,3,4,5: "))
input1=int(input("Enter first number here: "))
input2=int(input("Enter second number here: "))


if select == 1:
    print(f"{input1} + {input2} = {add(input1,input2)}")
elif select == 2:
    print(f"{input1} - {input2} = {sub(input1,input2)}")
elif select == 3:
    print(f"{input1} * {input2} = {mul(input1,input2)}")
elif select == 4:
    print(f"{input1} / {input2} = {div(input1,input2)}")
elif select == 5:
    print(f"({input1} + {input2})/2 ={avg(input1,input2)}")
else:
    print(f"you entered {select} invalid operations,plz try again!")

