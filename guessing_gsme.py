import random

secret_number = random.randint(1, 10)
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

guess = int(input("Your guess: "))

if guess == secret_number:
    print("🎉 Correct! You guessed the number!")
elif guess < secret_number:
    print("Too low! Try again next time.")
else:
    print("Too high! Try again next time.")

print("The secret number was:", secret_number)
