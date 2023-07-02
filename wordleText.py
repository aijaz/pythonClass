import game

history_of_guesses = []

def add_to_history_and_print(the_word, the_result):
    history_of_guesses.append((the_word, the_result))
    for r in history_of_guesses:
        for char in r[0]:
            print(char, end=" ")
        print("")
        print(r[1])


secret_word = game.get_random_word()
number_of_guesses = 0
maximum_guesses = 6

while True:
    guess = input("Enter a word: ").strip().upper()
    number_of_guesses = number_of_guesses + 1
    if guess == secret_word:
        result = game.get_result(secret_word, guess)
        add_to_history_and_print(guess, result)
        print(f"That's correct! The word was {secret_word}")
        break

    print("That's wrong")
    if number_of_guesses < maximum_guesses:
        print("Try again.")
        result = game.get_result(secret_word, guess)
        add_to_history_and_print(guess, result)
    else:
        print(f"Sorry. You ran out of guesses. The word is {secret_word}.")
        break

print("Game Over")
