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

valid_gameplay("<enter> for # of rounds or enter an integer for # of rounds")

