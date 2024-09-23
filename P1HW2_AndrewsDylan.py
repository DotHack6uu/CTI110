# Dylan Andrews
# Date: 09/23/2024
# P1HW2
# This program calculates expenses and compares them to the user's budget.



print("\n-----This program calculates and displays travel expenses----\n")
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("Last, how much do you need for food? "))



#----------------------------------------------------------------------------------------------------


total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses



#----------------------------------------------------------------------------------------------------

print("\n------------Travel Expenses------------")

print(f"Location: {destination}")

print(f"Initial Budget: {budget}")

print(f"\nFuel: {gas_expense}")

print(f"Accommodation: {accommodation_expense}")

print(f"Food: {food_expense}")

print(f"\nRemaining Balance: {remaining_budget}")
