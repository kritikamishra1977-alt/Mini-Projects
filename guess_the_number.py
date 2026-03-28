import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = input("Enter your guess: ")

    # Make sure the input is a number
    if not guess.isdigit():
        print("❌ Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number:
        print("📉 Too low!")
    elif guess > number:
        print("📈 Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break