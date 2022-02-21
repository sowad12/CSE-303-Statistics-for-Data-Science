


import math
def check(a,b,c):
    if a + b > c and a + c > b and b + c > a:
         return 1;
    else:
        return 0;

x=int(input('First side: '))
y=int(input('second side: '))
z=int(input('third side: '))

if(check(x,y,z)==1):
     s = (x + y + x) / 2
     ans= math.sqrt(s *(s - x) *(s - y)* (s - z))
     print('{0:.2f}'.format(ans))
     
else:
    print('Invalid triangle')        

