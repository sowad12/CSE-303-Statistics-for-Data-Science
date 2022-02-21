# Given a positive integer N (read from the user), write a Python program to calculate the value of the
# following series.
#   1^2+2^2+3^2+...+N^2
#sol: 1^2+2^2+3^2+...+N^2=n(n+1)(2n+1)/6

n=int(input('Enter positive integer:'))
result=int((n*(n+1)*(2*n+1))/6)
print("Result:",result)
