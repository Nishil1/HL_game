import random
def show_instructions():
    while True:
        question = input("Have you played the game before? ")
        instructions = "Show Instructions"

        if question == "yes" or question == "y":
            print(instructions)
            return
        elif question == "no" or question == "n":
            print(instructions)
            return
        else:
            print("Please enter yes/no")

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




def check_user_guess(question):
    response = input(question)
    correct_number = random.randint(1,100)




guess_number = num_check("Guess the number between 1-100: ")

