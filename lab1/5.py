# 5.Given a positive integer N (read from the user), write a Python program to check if the number is
# prime or not. Define a function named as prime_find_<your-student-id> in your program.


def prime_find_2018360081(n):
    prime = [True for i in range(n+100)]
    p=2
    for p in range(p, n, p*p): # for (int p = 2; p * p <= n; p++) ->c++
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
  
    print('Number is prime')if(prime[n]) else print('Number is not prime')
 
 
n=int(input('Integer type input:')) 
prime_find_2018360081(n)            

