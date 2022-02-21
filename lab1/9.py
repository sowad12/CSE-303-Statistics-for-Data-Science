# 9. Given a list of numbers (hardcoded in the program), write a Python program to find the largest and
# smallest element of the list. Define two functions largest_number_<your-student-id> and
# smallest_number_<your-student-id> in your program. Do not use any built-in function.


import sys

def largest_number_2018360081(li):
    min=-sys.maxsize - 1
    for i in range(len(li)):
         if(min<li[i]):
             min=li[i]           
    return min     
     
def smallest_number_2018360081(li):
    max= sys.maxsize
    for i in range(len(li)):
         if(max>li[i]):
             max=li[i]           
    return max       
     
s="10,20,30,40,50,1,15,-5,100,66,7"
li=[int(x) for x in s.split(',')]     
print('Largest Element:',largest_number_2018360081(li))
print('Smallest Element:',smallest_number_2018360081(li))