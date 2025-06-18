import random

secret = random.randint(1, 100)
while True:
    guess = int(input("Your guess"))
    if secret == guess:
        print("correct")
        break
    else:
        print("Try again")
