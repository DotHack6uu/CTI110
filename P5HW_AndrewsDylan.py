#Dylan Andrews
#19NOV2024
#P5HW - MathQuiz
#This code asks if you want to test your addition/subtracting skills
#picking one prompts a little quiz
#The code will continue until the user selects the option to exit.


####################################################################################################

import random

####################################################################################################

def addition_quiz():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"\n  {num1}")
    print(f"+ {num2}")
    guess_count = 0

    while True:
        try:
            user_answer = int(input("Enter your answer: "))
            guess_count += 1
            if user_answer == correct_answer:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guess_count}")
                break
            elif user_answer < correct_answer:
                print("Sorry, guess is too low.")
            else:
                print("Sorry, guess is too high.")
        except ValueError:
            print("Please enter a valid number.")

####################################################################################################

def subtraction_quiz():
   
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    if num1 < num2:
        num1, num2 = num2, num1
    correct_answer = num1 - num2
    print(f"\n  {num1}")
    print(f"- {num2}")
    guess_count = 0

    while True:
        try:
            user_answer = int(input("Enter your answer: "))
            guess_count += 1
            if user_answer == correct_answer:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guess_count}")
                break
            elif user_answer < correct_answer:
                print("Sorry, guess is too low.")
            else:
                print("Sorry, guess is too high.")
        except ValueError:
            print("Please enter a valid number.")
####################################################################################################
def main():
   
    while True:
        print("\nWelcome to Math Quiz")
        print("\nMAIN MENU")
        print("---------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        try:
            choice = int(input("\nPlease choose one of the menu options: "))
            if choice == 1:
                addition_quiz()
            elif choice == 2:
                subtraction_quiz()
            elif choice == 3:
                print("Thank you for playing...\nBye!!")
                break
            else:
                print("Error: Invalid selection. Please enter 1, 2, or 3.")
        except ValueError:
            print("Error: Invalid input. Please enter a number (1, 2, or 3).")

####################################################################################################
if __name__ == "__main__":
    main()
