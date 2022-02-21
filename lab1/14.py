# 14. Given a string, write a python program to check if it is palindrome or not. Define a function named
# palindrome_checker_<your-student-id> in your program.

def palindrome_checker_2018360081(li,s):
    li.reverse()
    flag=0
    for x in range(len(li)):
        if(li[x]!=s[x]):
            flag=1
    return flag        
    
s='redivider'
li=[s[x] for x in range(len(s))]
result=palindrome_checker_2018360081(li,s)
print("{} is Palindrome".format(s))if(result==0) else print("{} is not Palindrome".format(s))   