# Funtions go here
def num_check(question, low, high) :
    error = "please enter a integer between 1 and 10\n"

    while True:
        try:
            response = int(input(question))

            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")

def instructions():
    print("**** How to PLay ****")
    print()
    print("The rules of this game go here")
    print()
    return ""

played_before = yes_no("Have you played this game before?")

if played_before == "no":
   instructions()

print("program continues")

# Main routine goes here
how_much = num_check("How much would like to play with?", 0, 10)
