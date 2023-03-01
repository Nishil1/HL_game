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