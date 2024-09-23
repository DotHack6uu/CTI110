# Dylan Andrews
# 2024-09-23
# P1HW1
# A code that performs exponentiation and basic addition then subtraction from user input



print("\n-----Calculating Exponents----\n")



base = int(input("Enter the base integer: "))


exponent = int(input("Enter the exponent integer: "))


result = base ** exponent


print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

#---------------------------------------------------------------------

print("-----Addition and Subtraction----\n")

num1 = int(input("Enter the first integer: "))

num2 = int(input("Enter the second integer: "))

num3 = int(input("Enter the third integer: "))


sum_result = num1 + num2
final_result = sum_result - num3

print(f"\n{num1} + {num2} - {num3} is equal to {final_result} !! ")
