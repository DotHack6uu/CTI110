# Dylan Andrews
# 2024-10-03
# P2LAB1
# Calculates the diameter, circumference, and area of a circle based on users input of a radius.

#add math so it works
import math

# Ask user for radius 
radius = float(input("What is the radius of the circle? "))

# calculations 
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# gives the diameter, circumference, and area of the user input for radius
print(f"\nThe diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
