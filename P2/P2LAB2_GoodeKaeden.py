#Kaeden Goode
#09/17/2026
#P2LAB2
#Dictionary Knowledge Test

#Initial Dict
mpg = {"Camaro":18.21,"Prius":52.36,"Model S":110.0,"Silverado":26.0}

keys = mpg.keys()
print("\n\n-----------------------------------")

#Display List
print("\n\n\nThese are the availiable vehicles: ", keys)

#Vehicle Input
vehicle = input("\nEnter a vehicle to see it's mpg: ")

#MPG List
print("\nThe ", vehicle," gets ", mpg[vehicle], " mpg.",sep="")

#Miles Request
miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

gallons = miles / mpg[vehicle]

#Final Print
print(f"\n{gallons:.2} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")