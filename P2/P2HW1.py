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
print(f"Location: \t\t${destination}")
print(f"Initial budget: \t${budget:.2f}")
print(f"Fuel: \t\t\t${gas:.2f}")
print(f"Accommodation: \t\t${housing:.2f}")
print(f"Food: \t\t\t${food:.2f}")
print("------------------------------------------------------")
print(f"\nRemaining Balance: \t${balance:.2f}")