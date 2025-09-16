import random

guess_number = random.randint(1, 100)

print("Computer generated a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < guess_number:
            print("Too low!")
        elif guess > guess_number:
            print("Too high!")
        else:
            print("🎉 Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number between 1 and 100.")
