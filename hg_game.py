import random
words = ["apple", "python", "chair", "school", "flower"]

# Randomly choose one word
word = random.choice(words)
guessed_letters = []
attempts = 6

print(" Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print(" Good guess!")
    else:
        print(" Wrong guess!")
        attempts -= 1

    # Show current word progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    print("Attempts left:", attempts)

    # Check for win condition
    if "_" not in display:
        print("\n You won! The word was:", word)
        break
else:
    print("\n You lost. The correct word was:", word)
