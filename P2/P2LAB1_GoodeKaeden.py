#Kaeden Goode
#9/15/2026
#CTI-110-0001
#P2LAB1 - Libraries and f-strings

import math

#get radius from user
radius = float(input("Please give the radius: "))

#math
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius**2)

print("\n\n-----Calculations-----")

print("\n\nWhat is the radius of the circle? ",radius,sep="")

print(f"The diameter of the circle is {diameter:.1f}")

print(f"The circumference of the circle is {circumference:.2f}")

print(f"The area of the circle is {area:.3f}")