# 1. Given two integer numbers, write a Python program to return their product. If the product is greater
# than 1000, then return their sum. Read inputs from the user.


def choice(a,b):
    product=a*b
    if(product>1000):
        return (a+b)
    return product

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
print('Result:',choice(a,b))
