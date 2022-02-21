#2. Write a Python program to find the area and perimeter of a circle. Read inputs from the user.
import math
def area(r):
    return math.pi*(r**2)

def perimeter(r):
    return 2*math.pi*r

r=float(input("Enter Radius:"))

print('Area:',round(area(r),2))
print('Perimeter:',round(perimeter(r),2))