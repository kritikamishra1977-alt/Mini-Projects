import random

# Movies with hints
movies = {
    "GULLY BOY": "Rapper based movie",
    "DANGAL": "Wrestling / sports movie",
    "PADMAN": "Social awareness film",
    "ROCKSTAR": "Music based story",
    "SULTAN": "Wrestling movie",
    "DON": "Crime thriller"
}

# Select random movie
movie = random.choice(list(movies.keys()))
hint = movies[movie]

total_chances = 9
guessed_movie = ""

# Create blank movie name
for ch in movie:
    if ch == " ":
        guessed_movie += " "
    else:
        guessed_movie += "-"

print("Bollywood Guessing Game")

while total_chances > 0:
    print("\nGuess the Movie:", guessed_movie)
    print("Attempts left:", total_chances)

    # show hint only when 2 chances left
    if total_chances == 2:
        print("Hint:", hint)

    letter = input("Enter a letter: ").upper()

    # validation
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single valid letter")
        continue

    if letter in guessed_movie:
        print("Letter already guessed")
        continue

    if letter in movie:
        for i in range(len(movie)):
            if movie[i] == letter:
                guessed_movie = guessed_movie[:i] + letter + guessed_movie[i+1:]
        print("Correct guess")
    else:
        total_chances -= 1
        print("Wrong guess")

    # win condition
    if guessed_movie == movie:
        print("\nYou guessed the movie:", movie)
        break

else:
    print("\nGame Over")
    print("The correct movie was:", movie)