

def result (num,cr):
    if (num>=95 and num<=100):
        gpa=4.0
        print("Grade:A")
    elif (num>=85 and num<=95): 
        gpa=3.5
        print("Grade:B")
    elif (num>=70 and num<=85): 
        gpa=3.0
        print("Grade:C")
    elif (num>=60 and num<=70): 
        gpa=2.5
        print("Grade:D")
    elif (num>=0 and num<=60):
        gpa=0.0
        print("Grade:F") 
    return gpa*cr

f1 = float(input("Enter First course mark: "))
c1 = float(input("Enter First course credit: "))
x = result(f1,c1)
f2 = float(input("Enter Second course mark: "))
c2 = float(input("Enter Second course credit: "))
y = result(f2,c2)
f3 = float(input("Enter Third course mark: "))
c3= float(input("Enter Third course credit: "))
z = result(f3,c3)
term =float((x+y+z)/(c1+c2+c3))
print('Term GPA is:{0:.2f}'.format(term))
