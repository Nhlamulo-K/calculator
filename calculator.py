import math

num1=float(input('Enter first number: '))
num2=float(input('Enter second number: '))
operator=input('Enter operator: ')

def math():
    if operator== '+':
        num=num1+num2
    elif operator=='-':
        num=num1-num2
    elif operator=='*':
        num=num1*num2
    elif operator=='/':
        if num2!=0:
            num=num1/num2
        else:
            raise ValueError('cannot divide by zero')
    elif operator=='%':
        num=num1%num2
    elif operator=='sqrt':
        num=math.sqrt(num1)
    else:
        print('Invalid operator')
    print(num)
math()
