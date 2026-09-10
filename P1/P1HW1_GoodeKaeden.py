# Kaeden Goode
# 9/10/2026
# P1HW1
# A Simple Calculator

print("-----Calculating Exponents-----")
a = int(input("\n\nEnter an integer as the base value: "))
b = int(input("Enter an integer as the exponent: "))

calc1 = a**b

print("\n\n",a," raised to the power of ",b," is ",calc1,"!!",sep="")

print ("\n\n-----Addition and Subtraction-----")

x = int(input("\n\nEnter a starting integer: "))
y = int(input("Enter an integer to add: "))
z = int(input("Enter an integer to subtract: "))

calc2 = x+y-z

print("\n\n",x," + ",y," - ",z," is equal to ",calc2,sep="")
