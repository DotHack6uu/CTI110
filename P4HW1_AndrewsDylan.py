#Dylan Andrews
#Date 10Nov2024
#P4HW1
#The code collects & validates data. takes away lowest grade and gives it a letter grade

#--------------------------------------------------------------------------------------------------------#
#1.Asks the user how many scores they want to enter
#2.Makes an empty list for storing scores
#3.Loops the number of times specified by the user(step3), enter score,if true keep if not say bad and reenter
#4.After collecting all scores: shows and deletes lowest score, and show list
#5.Display the average and letter grade
#--------------------------------------------------------------------------------------------------------#




##########################################################################

num_scores = int(input("How many scores do you want to enter?! "))



##########################################################################

a_list_of_user_scores = []



##########################################################################

for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:
                a_list_of_user_scores.append(score)
                break
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("Please enter a valid number.")

##########################################################################

lowest_score = min(a_list_of_user_scores)
a_list_of_user_scores.remove(lowest_score)
average_score = sum(a_list_of_user_scores) / len(a_list_of_user_scores)

##########################################################################
if average_score >= 90:
    grade = 'You Gotta A!'
elif average_score >= 80:
    grade = 'You Gotta B'
elif average_score >= 70:
    grade = 'You Gotta C'
elif average_score >= 60:
    grade = 'You Gotta D'
else:
    grade = 'You Gotta F'

#########################################################################
print("\n------------Results-----------")
print(f"Lowest Score: {lowest_score:.1f}")
print(f"Modified List: {a_list_of_user_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade: {grade}")
print("--------------------------------")
