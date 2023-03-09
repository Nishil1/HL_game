import random
import math


# checks for valid numbers for lower, higher and user guess
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
                # check if user input is valid
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}")
                    continue
                    # checks whether the high number is greater than low number
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more than or equal to {low}")
                    continue
                    # returns response if all above conditions are met
            return response
        # checks for Value error
        except ValueError:
            print("Please enter an integer")
            continue


# makes sure number of rounds is valid
def round_valid(question):
    error = "Please enter an integer greater than 1"
    while True:
        try:
            # asks question
            response = int(input(question))
            # checks if response is less than one
            if response < 1:
                print(error)
            else:
                # returns response if above conditions are met
                return response
            # checks for Value error
        except ValueError:
            print(error)


# Instructions function


def show_instructions():
    while True:
        # asks question
        var_question = input("Have you played the game before? ").lower()
        instructions = "Enter a higher and a lower number, " \
                       "a secret number will be randomly generated with limited amount of guesses. " \
                       "Can you win the game?"
        # checks for 2 possible answers
        if var_question == "yes" or var_question == "y":
            return
        elif var_question == "no" or var_question == "n":

            # shows instructions
            print(instructions)
            return
        # if input is invalid
        else:
            print("Please enter yes/no")


# Main routine starts here
print("***************************************")
print("**** Welcome to Higher, lower game ****")
print("***************************************")
print()
print()
# shows instructions
show_instructions()
# Game history list
game_history = []
# ask use for number of rounds
decided_number_of_rounds = round_valid("How many rounds: ")
# Variables counting rounds played & number of guesses done
number_of_rounds_played = 1
number_of_guesses_done = 0
# Gets the higher & lower numbers
lower_number = num_check("Lower number: ")
higher_number = num_check("Higher number: ", lower_number + 1)
# Calculate number of guesses allowed
ranges = higher_number - lower_number + 1
max_raw = math.log2(ranges)
max_upped = math.ceil(max_raw)
maximum_guesses = max_upped + 1
# Game loop
while number_of_rounds_played <= decided_number_of_rounds:
    # Displays rounds number & number of guesses available to the user
    print(f"--------------- Round: {number_of_rounds_played} ---------------")
    print(f"Number of guesses: {maximum_guesses}")
    number_of_guesses_done = 0
    # already guessed list, makes sure no duplicates are entered
    already_guessed = []
    # Generates secret number for user to guess
    secret_number = random.randint(lower_number, higher_number)
    game_won = False
    while number_of_guesses_done < maximum_guesses:
        # Takes user guess
        user_guessed_number = num_check("Guess: ", lower_number, higher_number)
        # Checks for duplicates & outputs error if found
        if user_guessed_number in already_guessed:
            print("Oops you already guessed that, try another!")
            continue
        # Adds user guesses to already_guessed list to avoid duplicates
        already_guessed.append(user_guessed_number)
        number_of_guesses_done += 1
        # Checks for possible outcomes, low, high & wins
        if user_guessed_number < secret_number:
            print("***** Too low *****")
            print()
        elif user_guessed_number > secret_number:
            print("***** Too high *****")
            print()
        elif user_guessed_number == secret_number:
            print("!!!!! You got it !!!!!")
            print()
            # Adds user won to game history
            feedback = f"Round {number_of_rounds_played}: Won ({len(already_guessed)} guesses)"
            game_history.append(feedback)
            game_won = True
            break
        # Tells user updated number of guesses left
        print(f"Guesses left: {maximum_guesses - number_of_guesses_done}")
    # Reveals the Secret Number
    if game_won is False:
        print("Sorry no more guesses")
        print(f"The Secret Number was {secret_number}!!")
        # Adds user lost to game history
        feedback = f"Round {number_of_rounds_played}: Lost (ran out of guesses)"
        game_history.append(feedback)
    number_of_rounds_played += 1
# End of game(Thanks user & Game History)
print()
print()
print("**** Game History ****")
print()
for item in game_history:
    print(item)
print()
quit("Thanks for playing! ")
