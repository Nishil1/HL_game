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


show_instructions()

