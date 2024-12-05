# Dylan Andrews
# 2024-10-09
# P2HW2_AndrewsDylan.py
# This program collects grades from the user for six modules,
# Gathers the calculations and displays the lowest grade, highest grade, sum of grades, and average.

''' Pseudocode
# 1. Makeing a empty list to store the grades for low/hi/sum/adv.
# 2. User inputs grades for six modules and store them in the list.
# 3. Calculate the lowest grade using the min() function.
# 4. Calculate the highest grade using the max() function.
# 5. Calculate the sum of grades using the sum() function.
# 6. Calculate the average by dividing the sum by the number of grades.
# 7. Display the lowest, highest, sum, and average of the grades.
'''
# List to store grades
Class_grades = []

# Collect grades for six modules
Class_grades.append(float(input("Enter a grade for Module 1: ")))
Class_grades.append(float(input("Enter a grade for Module 2: ")))
Class_grades.append(float(input("Enter a grade for Module 3: ")))
Class_grades.append(float(input("Enter a grade for Module 4: ")))
Class_grades.append(float(input("Enter a grade for Module 5: ")))
Class_grades.append(float(input("Enter a grade for Module 6: ")))

# Calculate lowest, highest, sum, and average of grades
lowest_grade = min(Class_grades)
highest_grade = max(Class_grades)
sum_of_grades = sum(Class_grades)
average_grade = sum_of_grades / len(Class_grades)

# Display results with formatting
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade:.1f}")
print(f"Highest Grade:     {highest_grade:.1f}")
print(f"Sum of Grades:     {sum_of_grades:.1f}")
print(f"Average:           {average_grade:.2f}")
print("-------------------------------")
