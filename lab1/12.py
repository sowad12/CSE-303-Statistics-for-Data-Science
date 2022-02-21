# 12. Given a string and an integer number n, remove characters from a string starting from zero up to n
# and return a new string. N must be less than the length of the string. Read inputs from the user. Do
# not use any built-in function.

s = input("Enter String: ")
n = int(input("Enter a number : "))
cnt = 0
for element in s:
        cnt = cnt + 1
      
ns = ""           
for i in range(n,cnt):
    ns = ns+s[i]
    
print(f'New String : {ns}')

