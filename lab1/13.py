# 13. Given a string, find the count of the substring “CSE303” appeared in the given string. Do not use any
# built-in function.


s='HELLOFROMCSE303ADDNEWCOURSECSE303eeeeCSE303'
inc=1
cnt=0
for i in range(0,len(s),inc):
    if(s[i]=='C' and s[i+1]=='S'and s[i+2]=='E'and s[i+3]=='3'and s[i+4]=='0'and s[i+5]=='3'):
        inc=inc+5
        cnt=cnt+1
    else:
        inc=inc+1    
        
print('Total substring of CSE303:',cnt)        