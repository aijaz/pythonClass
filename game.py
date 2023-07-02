from random import choice

guessable_words = []


def get_random_word():
    global guessable_words
    with open("allwords.txt") as all_words_file:
        all_words = all_words_file.read().strip().upper()
        all_words_list = all_words.splitlines()

    with open("badwords.txt") as bad_words_file:
        bad_words = bad_words_file.read().strip().upper()
        bad_words_list = bad_words.splitlines()

    with open("commonwords.txt") as common_words_file:
        common_words = common_words_file.read().strip().upper()
        common_words_list = common_words.splitlines()

    guessable_words = [word for word in all_words_list if word not in bad_words_list]
    secret_words = [word for word in common_words_list if word not in bad_words_list]
    word = choice(secret_words)
    return word


#
# maximum_guesses = 6
# number_of_guesses = 0
# history_of_guesses = []
#

def get_result(secret_word, guess_word):
    
    result = []

    if len(secret_word) == 5 and len(guess_word) == 5:
        for i, letter in enumerate(guess_word):
            if secret_word[i] == letter:
                result.append('🟩')
            elif letter in secret_word:
                result.append('🟨')
            else:
                result.append('🟥')

    return "".join(result)


# def add_to_history_and_print(the_result):
#     history_of_guesses.append(the_result)
#     for r in history_of_guesses:
#         print(r)
#
#
# while True:
#     guess = input("Enter a word: ").strip().upper()
#     number_of_guesses = number_of_guesses + 1
#     if guess == random_word:
#         result = get_result(random_word, guess)
#         add_to_history_and_print(result)
#         print(f"That's correct! The word was {random_word}")
#         break
#
#     print("That's wrong")
#     if number_of_guesses < maximum_guesses:
#         print("Try again.")
#         result = get_result(random_word, guess)
#         add_to_history_and_print(result)
#     else:
#         print(f"Sorry. You ran out of guesses. The word is {random_word}.")
#         break
#
# print("Game Over")
