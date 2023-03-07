import random

tokens = ["unicorn", " horse", "zebra", "donkey"]
balance = 100

for item in range (0,20) :
    chosen = random.choice(tokens)
    print(chosen, end='\t')