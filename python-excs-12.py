import random

secret_number = random.randint(1, 100)
guess = None

print("Guess the number between 1 and 100!")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print("Correct! You guessed the number.")
