# 15. Given a two list of numbers (hardcoded in the program), create a new list such that new list should
# contain only odd numbers from the first list and even numbers from the second list.

s1="11,20,33,40,55,1,15,5,100,66,7"
s2="15,2,33,88,65,3,25,57,100,76,9"
li1=[int(x) for x in s1.split(',')]
li2=[int(x) for x in s2.split(',')]
li=[]
for i in range(len(li1)): 
     if(li1[i]%2!=0):
         li.append(li1[i])
    
for i in range(len(li2)): 
     if(li2[i]%2==0):
         li.append(li2[i])
         
li.sort()
print('New list:',li)           

  