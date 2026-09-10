# Kaeden Goode
# 9/10/2026
# P1HW2 CTI-110-0001
# I/O for Budgeting


# Request for the values to calculate
budget = float(input("\n\nPlease enter your budget: "))
destination = (input("Please enter your destination: "))
gas = float(input("Please enter how much you will spend on gas: "))
housing = float(input("Please enter how much you will spend on accomodation: "))
food = float(input("Please enter how much you will spend on food: "))


# the math adding expenses
expense = gas + housing + food
# then subtracting from initial total
balance = budget - expense


# check for if you are able to travel
if balance<0:
    print("\n\n------ERROR------")
    print("\nYou do not have enough budget in order to travel.")
#print breaking down expenses
else:
    print("\n\n--------Calculating--------")
    print("Location:", destination)
    print("Initial budget: ", budget)
    print("\nFuel: ", gas)
    print("Accomodation: ", housing)
    print("Food", food)

    print("\n\nYour remaining funds is $", balance)