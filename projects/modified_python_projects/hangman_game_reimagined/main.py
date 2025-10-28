import random

# Colors for terminal UI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Hangman ASCII art
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word list
word_list = ["bruiser", "catalyst", "browser", "diverse"]
chosen_word = random.choice(word_list)
lives = 6

# Placeholder setup
display = ["_" for _ in chosen_word]
correct_letters = []

# Game intro
print(BOLD + CYAN + "🎯 WELCOME TO HANGMAN! 🎯" + RESET)
print(YELLOW + "Try to guess the word before the man is hanged!" + RESET)
print(hangman[lives])
print(" ".join(display))
print()

# Main game loop
game_over = False
while not game_over:
    guess = input(CYAN + "🔤 Guess a letter: " + RESET).lower()

    if not guess.isalpha() or len(guess) != 1:
        print(RED + "⚠️ Please enter a single valid letter!" + RESET)
        continue

    if guess in correct_letters or guess in display:
        print(YELLOW + f"⚠️ You already guessed '{guess}'!" + RESET)
        continue

    # Build new display
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
            correct_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(RED + f"❌ Wrong guess! '{guess}' is not in the word." + RESET)
    else:
        print(GREEN + f"✅ Good guess! '{guess}' is in the word." + RESET)

    # Show progress
    print(hangman[lives])
    print(" ".join(display))
    print(YELLOW + f"Lives left: {lives}" + RESET)
    print()

    # End conditions
    if lives == 0:
        print(RED + BOLD + "💀 You lost! The word was: " + chosen_word.upper() + RESET)
        game_over = True
    elif "_" not in display:
        print(GREEN + BOLD + "🎉 Congratulations! You guessed the word!" + RESET)
        game_over = True
