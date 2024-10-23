#Dylan Andrews
#22OCT2024
#P3HW2_Salary_AndrewsDylan
#Calculates gross pay, and if overtime is worked

#Ask for name/hours/ rate of pay

employee_name = input("Enter employee's name: ")

hours_worked = float(input("Enter number of hours worked: "))

pay_rate = float(input("Enter employee's pay rate: "))
#overtime hours and pay

overtime_hours = 0

overtime_pay = 0

#Calculate regular and overtime pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    regular_hours = hours_worked

#normal regular pay
regular_pay = regular_hours * pay_rate

#geting gross pay
gross_pay = regular_pay + overtime_pay

#Display results
print("\n--------------------------------------------")

print(f"Employee name:   {employee_name}")

print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")

print("-----------------------------------------------------------")

print(f"{hours_worked:<15.2f}{pay_rate:<10.2f}{overtime_hours:<10.2f}{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<10.2f}")
