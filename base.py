import random

# shows instructions if needed
def show_instructions():
    while True:
        question = input("Have you played the game before? ").lower()
        instructions = "Show Instructions"

        if question == "yes" or question == "y":
            return

        elif question == "no" or question == "n":
            print(instructions)
            return

        else:
            print("Please enter yes/no")


# checks whether user gameplay is valid. Eg.(infinite/# of rounds of gameplay)
def valid_gameplay(question):
    while True:

        response = input(question)
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
def num_check(question):
    while True:
        try:
            response = int(input(question))

            if 1<= response <= 100:
                return response
            else:
                print("Please enter a guess between 1 and 100")
        except ValueError:
            print("Please enter a whole integer")



# Main routine starts here





secret_number = random.randint(1, 100)
number_of_rounds_played = 1
already_guessed = 0
number_of_guesses_allowed = 9


amount_of_rounds = valid_gameplay("<enter> to infinite mode or enter a # of rounds to play")

if amount_of_rounds != "":
    mode = "regular"
else:
    mode = "infinite"
    amount_of_rounds = 3



while number_of_rounds_played < amount_of_rounds:
    print(f"Round: {number_of_rounds_played}")
    if already_guessed <= number_of_guesses_allowed:


            if mode == "infinite":
                amount_of_rounds += 3

            user_guess = num_check("Guess Number: ")
            already_guessed += 1


            if user_guess == secret_number:
                print("You Won")
                number_of_rounds_played += 1

            elif user_guess < secret_number:
                print("Oops too low, try higher")

            else:
                print("Oops too high, try lower")
    else:
        print("Sorry no more guesses allowed")
        print(f"Secret number was {secret_number}")
        







print("Thanks for playing")









