money = float(input("Enter the amount of money as a float: $"))

# Removing Decimal Spaces
money = money * 100


# Mathy Math, commented out was me experimenting with not using the Modulus

dollars = int( money // 100 )

money = money % 100
quarters = int(money // 25)

# quarters = int((money - dollars * 100) // 25)

money = money % 25
dimes = int(money // 10)

# dimes = int ((( money - dollars * 100) - quarters * 25 ) // 10)

money = money % 10
nickels = int(money // 5)

# nickels = int((((money - dollars * 100) - quarters *25) - dimes * 10) // 5)

money = money % 5
pennies = int(money // 1)

# pennies = int((((( money - dollars * 100 ) - quarters * 25) - dimes * 10) - nickels * 5) // 1)

# ======================================================================================================================

def changeCounter(coin, coinName):
    if coin == 1:
        print(f"{coin} {coinName}")
    elif coin > 0:
        if (coinName == "Penny" and coin > 1):
            coinName = "Pennie"
        print(f"{coin} {coinName}s")



# ======================================================================================================================


changeCounter(dollars, "Dollar")

changeCounter(quarters, "Quarter")

changeCounter(dimes, "Dime")

changeCounter(nickels, "Nickel")

changeCounter(pennies, "Penny")

if dollars <= 0 and quarters <= 0 and dimes <= 0 and nickels <= 0 and pennies <= 0:
    print("No Change.")

# ======================================================================================================================