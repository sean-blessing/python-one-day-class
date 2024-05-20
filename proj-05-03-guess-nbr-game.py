import random

MAX_NBR = 100

def main():
    print("Welcome to the Guess the number game!")
    print("=====================================")

    choice = "y"

    while choice.lower() == "y":
        print(f"\nI'm thinking of a number from 1 to {MAX_NBR}.")
        print("Try to guess it./n")
        
        the_number = get_rand_number()
        print("*****************")
        print(f"* DEBUG: # = {the_number} ")
        print("*****************\n")
        
        count = 0
        guess = 0
        
        while guess != the_number:
            guess = get_guess()
            count += 1
            if guess == the_number:
                print(f"You got it in {count} tries.")
                display_winner_message(count)
            else:
                diff = guess - the_number
                display_miss_message(diff)
        
        choice = input("\nTry again? (y/n) ")
    print("\nGoodbye")

def display_winner_message(count):
    if count <= 3:
        print("Great work! you area mathematical wizard!")
    elif count <= 7:
        print("Not too bad! You've got some potential.")
    else:
        print("What took you so long? Maybe you should take some lessons.")
    
def display_miss_message(diff):
    # nbr 35, guess 70, diff 35
    # nbr 35, guess 40, diff 5
    # nbr 35, guess 30, diff -5
    # nbr 35, guess 15, diff -20
    message = ""
    if diff < -10:
        message += "Way too low!!"
    elif diff < 0:
        message += "Too low!"
    elif diff > 10:
        message += "Way too high!!"
    elif diff > 0:
        message += "Too high!"
    message += " Guess again.\n"
    print(message)
    
def get_rand_number():
    return random.randint(1, MAX_NBR)
    
def get_whole_number(prompt):
    while True:
        try:
            whole_number = int(input(prompt))
            break
        except ValueError:
            print("Invalid entry. Please try again.")
            
    return whole_number

def get_guess():
    while True:
        guess = get_whole_number("\nEnter number: ")
        if guess < 1 or guess > 100:
            print("Guess out of range. Try again. ")
        else:
            break;
    return guess

if __name__ == "__main__":
    main()