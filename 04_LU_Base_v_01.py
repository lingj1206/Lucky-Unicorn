# Functions go here


# Main routine goes here
error = "please enter a whole number between 1 and 10"

while True:
    try:
        response = int(input("How much would like to play with?"))

        if 0 < response <= 10:
            print("you have asked to play with ${}".format(response))

        else:
            print(error)

    except ValueError:
        print(error)
