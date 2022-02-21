# 3. Write a Python program to calculate the compound interest based on the given formula. Read inputs
# from the user.
# A = P * (1 + R/100)^T

#  where P is the principle amount, R is the interest rate and T is time (in years).

# Define a function named as compound_interest_<your-student-id> in your program.

import math
def compound_interest_2018360081(p,r,t):
    return p*(math.pow((1+r/100),t))

p = float(input("Enter Principle: "))
r= float(input("Enter Interest rate: ")) 
t= int(input("Enter time in years: "))
   
print('Result: {:.2f}'.format(compound_interest_2018360081(p,r,t)))