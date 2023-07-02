from random import choice

guessable_words = []


def get_random_word():
    global guessable_words
    with open("allwords.txt") as all_words_file:
        all_words = all_words_file.read().strip().upper()
        guessable_words = all_words.splitlines()

    with open("commonwords.txt") as common_words_file:
        common_words = common_words_file.read().strip().upper()
        secret_words = common_words.splitlines()

    word = choice(secret_words)
    return word


#
# maximum_guesses = 6
# number_of_guesses = 0
# history_of_guesses = []
#

def get_result(secret_word, guess_word, character_state):
    if secret_word == guess_word:
        for c in secret_word:
            character_state[c] = '🟩'
        return '🟩🟩🟩🟩🟩'
    result = [None, None, None, None, None]

    number_available = {}

    # populate num_available
    for character in secret_word:
        if number_available.get(character) is None:
            number_available[character] = 1
        else:
            number_available[character] += 1

    for i in range(5):
        if guess_word[i] == secret_word[i]:
            result[i] = "🟩"
            character = guess_word[i]
            character_state[character] = "🟩"
            number_available[character] -= 1

    for i in range(5):
        if result[i] == "🟩":
            # we've already marked this:
            continue

        # At this point this is either "🟨" or "🟥"
        # We're only looking at characters that are no exact matches
        character = guess_word[i]
        if character in secret_word and number_available[character] > 0:
            result[i] = '🟨'
            if character_state.get(character) != '🟩':
                character_state[character] = '🟨'
            number_available[character] -= 1
        else:
            if character_state.get(character) is None:
                character_state[character] = '🟥'
            result[i] = '🟥'

    return "".join(result)

