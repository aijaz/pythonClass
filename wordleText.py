from xtermcolor import colorize

import game

history_of_guesses = []

def add_to_history_and_print(the_word, the_result, character_state):
    history_of_guesses.append((the_word, the_result))

    for r in history_of_guesses:
        for i, char in enumerate(r[0]):
            if r[1][i] == '🟩':
                print(colorize(r[0][i], ansi=234, ansi_bg=2), end="")
            elif r[1][i] == '🟨':
                print(colorize(r[0][i], ansi=234, ansi_bg=3), end="")
            else:
                print(colorize(r[0][i], ansi=234, ansi_bg=1), end="")
        print("")

    print("")
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ansi_bg = 245
        if character_state.get(c) == "🟩":
            ansi_bg = 2
        elif character_state.get(c) == '🟨':
            ansi_bg = 3
        elif character_state.get(c) == '🟥':
            ansi_bg = 1
        print(colorize(c, ansi=234, ansi_bg=ansi_bg), end=" ")
    print("")

secret_word = game.get_random_word()
number_of_guesses = 0
maximum_guesses = 6
character_state = {}

while True:
    guess = input("Enter a word: ").strip().upper()
    number_of_guesses = number_of_guesses + 1
    if guess == secret_word:
        result = game.get_result(secret_word, guess, character_state)
        add_to_history_and_print(guess, result, character_state)
        print(f"That's correct! The word was {secret_word}")
        break

    print("That's wrong")
    if number_of_guesses < maximum_guesses:
        print("Try again.")
        result = game.get_result(secret_word, guess, character_state)
        add_to_history_and_print(guess, result, character_state)
    else:
        print(f"Sorry. You ran out of guesses. The word is {secret_word}.")
        break

print("Game Over")


"""
ARISE
COUNT
TOOTH
MOTTO
"""