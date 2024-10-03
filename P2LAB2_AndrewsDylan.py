# Dylan Andrews
# 2024-10-03
# P2LAB2
# This program makes a dictionary with cars/trucks with their miles per gallon(MPG)
# Gives the mpg of the car/truck you input and asks how far you will drive and let you know much many gallons itd take to get there

# making dictionary car/truck and their MPG
car_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

#  keys from the dictionary
car_keys = car_mpg.keys()
print(car_keys)

# asks user to enter a car/truck 

vehicle = input("Enter a vehicle to see its MPG: ")

# checking if the input was valid
if vehicle in car_mpg:
    mpg = car_mpg[vehicle]
    print(f"\nThe {vehicle} gets {mpg} MPG.")
    
    # asks how far you think you will drive
    miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))
    
    # does mpg math
    gallons_needed = miles / mpg
    
    # shows how much gas you need to drive the miles user input
    print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
else:
    print(f"Sorry, {vehicle} is not in the list. Select one on the list.")
