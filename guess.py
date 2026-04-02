import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")
