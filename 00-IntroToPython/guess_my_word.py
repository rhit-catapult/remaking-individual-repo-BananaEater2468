import random
import nltk

from nltk.corpus import words
nltk.download('words')



def update_display_word(dw,sw,g): # Letter by letter, check to see if the letter is in the word
    new_display_word = ""
    for k in range(len(sw)):  # For all the c
        if g == sw[k]: # If the guess is equal to the secret word letter at pos "K"
            new_display_word += g
        else:
            new_display_word += dw[k]
    return new_display_word


def main():

    # Intro
    print("Guess My Word")

    #Random Word
    # word_options = [r.lower()]
    # secret_word = random.choice(word_options)
    # # print(secret_word) #TODO: Del

    def get_random_word():
        word_list = words.words()
        filtered_words = [word.lower() for word in word_list if word.isalpha() and 4 <= len(word) <= 7]
        return random.choice(filtered_words)

    secret_word = get_random_word()
    # Get String Length

    word_length = len(secret_word)
    # print(word_length) #TODO: Del

    # Print Display Word in *'s
    display_word = "*" * word_length

    # Empty List of Guessed Letters
    guessed_letters = []


    while display_word != secret_word: # loop
        guess = input("Guess a Letter: ") # Prompt For a Letter
        if len(guess) != 1: # Make sure guess is one letter
            print("Too many letters :(") # Response
            continue # we're done here
        if guess in guessed_letters: # Make sure the guess is not a duplicate
            print("You already guessed", guess, "!")
            continue
        guessed_letters.append(guess) # Add the guessed letter to the list of letters that have been guessed
        display_word = update_display_word(display_word, secret_word, guess)
        print(display_word)
    print("Yippee!")



    # Update display word - print it
    # if display_word = secret_word, break
    # Loop

    # print congrats and amount of guesses
# m
main()