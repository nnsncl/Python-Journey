import random

def guess(x):
    user_name = str(input("User name: "))
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Try again. Too low.")
        elif guess > random_number:
            print("Try again. Too high.")

    print(f"Yep. The number was {guess}. Gj {user_name}")
            
guess(100)