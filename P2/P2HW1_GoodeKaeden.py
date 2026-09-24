#Kaeden Goode
#9/23/2026
#P2HW1
#LIBRARIES

# Request for the values to calculate
budget = float(input("\n\nPlease enter your budget: "))
destination = (input("Please enter your destination: "))
gas = float(input("Please enter how much you will spend on gas: "))
housing = float(input("Please enter how much you will spend on accommodation: "))
food = float(input("Please enter how much you will spend on food: "))


# the math adding expenses
expense = gas + housing + food
# then subtracting from initial total
balance = budget - expense

#print breaking down expenses

print("\n\n-------------------Travel Expenses--------------------")
print(f"{'Location:':<40}{destination:<41}")
print(f"{'Initial budget:':<40}${budget:<41,.2f}")
print(f"{'Fuel:':<40}${gas:<41,.2f}")
print(f"{'Accommodation:':<40}${housing:<41,.2f}")
print(f"{'Food:':<40}${food:<41,.2f}")
print("------------------------------------------------------")
print(f"\n{'Remaining Balance:':<40}${balance:<41,.2f}")