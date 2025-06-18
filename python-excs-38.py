import random

best_score = None

while True:
    target = random.randint(1, 20)
    guess_count = 0

    print("\nGuess the number between 1 and 20!")

    while True:
        guess = int(input("Enter your guess: "))
        guess_count += 1

        if guess == target:
            print(f"Correct! You guessed it in {guess_count} tries.")
            if best_score is None or guess_count < best_score:
                best_score = guess_count
                print("This is your best score!")
            break
        elif guess < target:
            print("Too low.")
        else:
            print("Too high.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print(f"Your best score was {best_score} guesses.")
        break
