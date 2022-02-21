# 6. Given a positive integer n (read from the user), write a Python program to find the n-th Fibonacci
# number based on the following assumptions.
# Fn = Fn-1 + Fn-2 where F0 = 0 and F1 = 1

def fib(n):
    if(n<=1):
         return n 
    else:
        return fib(n-1)+fib(n-2)
    
n=int(input('Integer type input:')) 
print(str(n)+'th fibonaci number:',fib(n))     