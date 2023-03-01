import random

secret_number = random.randint(1, 100)
number_of_rounds_played = 1

amount_of_rounds = int(input("<enter> to infinite mode or enter a # of rounds to play"))

if amount_of_rounds != "":
    mode = "regular"
else:
    mode = "infinite"


while number_of_rounds_played <= amount_of_rounds and mode == "regular":
    if mode == "infinite":
        amount_of_rounds += 1

    print(f"Round: {number_of_rounds_played}")

    user_guess = int(input("Guess Number: "))

    if user_guess == secret_number:
        print("You Won")
    elif user_guess < secret_number:
        print("Oops too low, try higher")

    else:
        print("Oops too high, try lower")
    number_of_rounds_played += 1
