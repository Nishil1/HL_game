import random
import math


# shows instructions if needed
def show_instructions():
    while True:
        var_question = input("Have you played the game before? ").lower()
        instructions = "Show Instructions"
        if var_question == "yes" or var_question == "y":
            return
        elif var_question == "no" or var_question == "n":
            print(instructions)
            return
        else:
            print("Please enter yes/no")


# checks whether user gameplay is valid. Eg.(infinite/# of rounds of gameplay)
def valid_gameplay(info):
    while True:
        response = input(info)
        if response != "":
            try:
                response = int(response)
                if response < 1:
                    print("Please enter a whole # greater than 1")
                    continue
            except ValueError:
                print("Please enter a whole #")
                continue
        return response


# checks whether user guess is valid
def num_check(info, low=None, high=None):
    situation = ""
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"
    while True:
        try:
            response = int(input(info))
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}")
                    continue
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more than or equal to {low}")
                    continue
            return response
        except ValueError:
            print("Please enter an integer")
            continue


def num_of_guesses(high, low):
    ranges = high - low + 1
    max_raw = math.log2(ranges)
    max_upped = math.ceil(max_raw)
    maximum_guesses = max_upped + 1
    return maximum_guesses


def decide_winner(user_guess, secret_num):
    if user_guess < secret_num:

        print("----- Too low -----")
        return False
    elif user_guess > secret_num:
        print("----- Too high -----")

        return False
    else:
        print("----- You got it!! -----")
        outcome == "won"
        return True
    outcome == "lost"


# function provides gameplay components for playing the game
def play():
    already_guess = []

    # function to generate secret number
    secret_number = random.randint(lower_number, higher_number)
    # calculate the number of guesses and display to user
    current_guess_count = 1
    print()
    print(f"Maximum number of guesses allowed: {number_of_guesses}")
    print()
    print(f"---- Round: {number_of_rounds_played} ----")

    print()
    while current_guess_count <= number_of_guesses:
        # user enters the guessed secret number
        user_guessed_number = num_check("Guess: ", lower_number, higher_number)
        if user_guessed_number in already_guess:
            print("You already guessed that number, try another number")
            continue
        already_guess.append(user_guessed_number)
        # functon taking user_guessed_number,secret_number as parameter to say the guesses is too high or low or correct
        winner = decide_winner(user_guessed_number, secret_number)
        if winner is True:
            break;
        else:
            current_guess_count += 1
    else:
        print("Sorry no more guesses left")
        print(f"The secret number was {secret_number}")
        # adds result to the rounds_result for game stats



# Main routine starts here
print("***************************************")
print("**** Welcome to Higher, lower game ****")
print("***************************************")
print()
print()

print()
show_instructions()
print()
# checks mode of gameplay
num_of_rounds = valid_gameplay("Press <enter> to enter infinite mode or enter an amount of rounds: ")
print()
# ask user for highest and lowest
lower_number = num_check("Lower number: ")
higher_number = num_check("Higher number: ", lower_number + 1)
print()
number_of_guesses = num_of_guesses(higher_number, lower_number)
game_history = []
number_of_rounds_played = 1
# if infinite mode
while num_of_rounds == "":
    play();
    # ask user if want to continue or exit
    print()
    question = input("Press <enter> to play again or any key to quit: ")
    if question == "":
        number_of_rounds_played += 1
        continue
    else:
        break
number_of_rounds_played = 1
outcome = ""
feedback = f"Round {number_of_rounds_played}: {outcome}"

game_history.append(feedback)

# if regular mode
while num_of_rounds != "" and number_of_rounds_played <= num_of_rounds:
    play();
    number_of_rounds_played += 1

for item in game_history:
    print(item)