# 8. Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
# the even-indexed elements in the list.

s="10,20,30,40,50"
li=[int(x) for x in s.split(',')]
sum=0
for i in range(len(li)):
    if(i%2==0):
        sum+=li[i]
print("List Sum:",sum)    