import math
import random

def update_displayword(dw,sw,g):


    # Letter by letter, check to see if the letter is in the word

def main():

    # Intro
    print("Guess My Word")

    #Random Word
    word_options = ['burger', 'funky', 'frogs', 'block']
    secret_word = random.choice(word_options)
    print(secret_word) #TODO: Del

    # Get String Length
    word_length = len(secret_word)
    print(word_length) #TODO: Del

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




    # Update display word - print it
    # if display_word = secret_word, break
    # Loop }

    # print congrats and amount of guesses

main()