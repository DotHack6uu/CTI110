#Dylan Andrews
#19OCT2024
#P3HW1_AndrewsDylan
#This program takes six module grades, determines the average, and displays the letter grade for the average.

#Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

#Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

#adds line
print("\n----------------------Results------------------------------")

#lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

#shows results
print(f"\nLowest Grade:  {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average Grade: {avg:.2f}")

#lineeee
print("-----------------------------------------------------------")

#Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')



