import random

# main routine goes here

STARTING_BALANCE = 10

balance = STARTING_BALANCE
# testing loop to generate 20 tokens
for item in range(0, 5):
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

    print()
    print(f"Starting Balance: ${STARTING_BALANCE}")
    print(chosen)
    print(balance)
    print(f"Final Balance: ${balance}")
