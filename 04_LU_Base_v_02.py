import random

# Functions go here


def num_check(question, low, high):
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
    print()
    print("**** How to PLay ****")
    print()
    print("This game is easy to play")
    print("All you need to do is pick a amount of money you would like to play with")
    print("between $1 and $10 not including cents")
    print("After that you press <enter> to start the game and when starting the next round")
    print()
    return ""


def statement_generator(statement, decoration, lines=None):

    sides = decoration * 3

    statement = f"{sides}{statement}{sides}"
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


played_before = yes_no("Have you played this game before?")

if played_before == "no":

    instructions()

print()

# Main routine goes here
how_much = num_check("How much would like to play with?", 0, 10)

balance = how_much

rounds_played = 0

play_again = ''
while play_again == '':

    play_again = input("press <ENTER> to play  or 'xxx' to quit...").lower()
    if play_again == "xxx":
        break

    # increase #of rounds played
    rounds_played += 1

    # print round number
    print(f"*** Round # {rounds_played} ***")
    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        prize_decoration = "!"
        chosen = "unicorn"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            prize_decoration = "H"
            chosen = "horse"
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = f"You got a {chosen}. Your balance is ${balance:.2f}"

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print(f"Final Balance ${balance:.2f}")
