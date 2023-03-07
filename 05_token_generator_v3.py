import random

tokens = ["unicorn", " horse", "zebra", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

for item in range(0, 100):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print()
print(f"Starting Balance: ${STARTING_BALANCE}")
print(f"Final Balance: ${balance}")
