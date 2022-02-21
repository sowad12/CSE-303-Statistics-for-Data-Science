# 11. Given a string, display only those characters which are present at an even index number. Read inputs
# from the user.

s=input('Input a string:')
rs=''

for x in range(len(s)):
     if((x+1)%2==0):
         rs=rs+str(s[x])
print('Result:',rs)         