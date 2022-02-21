# 10. Given a list of numbers (hardcoded in the program), write a Python program to find the second
# largest element of the list.

s="10,20,30,40,50,1,15,-5,100,66,7"
li=[int(x) for x in s.split(',')]     
li.sort()
print("Second largest element:{}".format(li[len(li)-2]))

