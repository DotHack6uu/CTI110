#Dylan Andrews
#10Nov2024
#P4HW2_Salary_AndrewsDylan
#Code figures out gross pay for multiple employees, overtime, regular, and gross pay totals


##################################################################################################################################

# 1. Asks user for data about employees and calculates total overtime pay, total regular pay, and total gross pay.
# 2. Start a loop to collect employee information
# 3. Adds up pay based on hours worked/overtime
# 4. Add the employee's overtime pay, regular pay, and gross pay
# 5. Display the individual employee's data
# 6. Once the loop ends code will display a table of employees and their data combined

##################################################################################################################################


##################################################################################################################################

total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

##################################################################################################################################

while True:
    employee_name = input("Enter an employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    overtime_hours = 0
    overtime_pay = 0

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

##################################################################################################################################
    print("\n--------------------------------------------")
    print(f"Employee name:   {employee_name}")
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
    print("-----------------------------------------------------------")
    print(f"{hours_worked:<15.2f}{pay_rate:<10.2f}{overtime_hours:<10.2f}{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<10.2f}")
    print("\n--------------------------------------------")

##################################################################################################################################

print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
