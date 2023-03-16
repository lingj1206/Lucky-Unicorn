import random

# get balance for testing purposes
balance = 10

rounds_played = 0

play_again = input("press <ENTER> to play ...").lower()
while play_again == '':

    # increase #of rounds played
    rounds_played += 1

    # print round number
    print(f"*** Round # {rounds_played} ***")
    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "unicorn"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    # print(chosen)
    # print(balance)
    print(f'You got a {chosen}.  Your balance is ${balance:.2f}')
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print(f"Final Balance ${balance:.2f}")
