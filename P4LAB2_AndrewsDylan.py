#Dylan Andrews
#6nov24
#P4LAB2_Andrewsdylan
#multiply tabel 

#inputing multi table code w/ for
def display_multiplication_table(number):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

#whilelooooop
def main():
    while True:  #Whileeeee
        try:
            user_input = int(input("Enter an integer (zero or higher): "))  # #input
            
            if user_input < 0:
                print("Try Again with a positive number.")
            else:
                display_multiplication_table(user_input)  #shows tabel
            
            #wana do it again
            run_again = input("\nWana See Me Do It Again? (yes/no): ").strip().lower()
            if run_again != 'yes':
                print("Good Night Im Sleepy")
                break  # Exit the loop if user does not want to run again

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
