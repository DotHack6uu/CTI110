#Dylan Andrews
#10-19-24
#P3LAB_AndrewsDylan
#Gives quanity of dollars, quarters, dimes, nickels, and pennies for user input

def calculate_change(amount):
    if amount == 0:
        print("No change")
        return
    
    #$ to cents
    cents = int(round(amount * 100))
    
    #math to make change
    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents

    #results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")

#user input
try:
    amount = float(input("Enter the amount of money as a float: $"))
    calculate_change(amount)
except ValueError:
    print("Please enter a valid float value.")
