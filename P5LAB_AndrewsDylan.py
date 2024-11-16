#Dylan Andrews
#11Nov24
#P5LAB Self-Checkout Simulation
#This code gives a random amount due and prompts you to pay and gives you correct change

########################################################################################

import random

########################################################################################

def disperse_change(change):
    dollars = int(change // 1)
    change -= dollars * 1

    quarters = int(change // 0.25)
    change -= quarters * 0.25

    dimes = int(change // 0.10)
    change -= dimes * 0.10

    nickels = int(change // 0.05)
    change -= nickels * 0.05

    pennies = int(change // 0.01)

########################################################################################
    print("\nChange breakdown:")
    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")

########################################################################################
def main():

    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${total_owed:.2f}")


    payment = float(input("How much cash will you put in the self-checkout? "))
    while payment < total_owed:
        print("The amount entered is less than the total owed. Please try again.")
        payment = float(input("How much cash will you put in the self-checkout? "))


    change = round(payment - total_owed, 2)
    print(f"Change: ${change:.2f}")


    disperse_change(change)

########################################################################################


if __name__ == "__main__":
    main()
########################################################################################
