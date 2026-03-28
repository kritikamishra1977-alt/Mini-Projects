import random

# normal life + thode long words
word_list = [
    "umbrella", "chocolate", "computer", "notebook", "telephone",
    "vegetable", "furniture", "building", "festival", "hospital",
    "breakfast", "education", "sandwich", "calendar", "medicine"
]

secret_word = random.choice(word_list)

guessed = []
chances = 6

print("Welcome to Hangman Game")

while chances > 0:
    display = ""

    for ch in secret_word:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Chances left:", chances)

    user_input = input("Guess a letter: ").lower()

    if len(user_input) != 1:
        print("Enter only one letter")
        continue

    if user_input in guessed:
        print("Already guessed")
        continue

    guessed.append(user_input)

    if user_input in secret_word:
        print("Good guess")
    else:
        print("Wrong guess")
        chances -= 1

    done = True
    for ch in secret_word:
        if ch not in guessed:
            done = False
            break

    if done:
        print("\nYou win! Word was:", secret_word)
        break

if chances == 0:
    print("\nYou lost! Word was:", secret_word)