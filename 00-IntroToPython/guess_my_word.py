import math
import random

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


# Loop {
# Prompt For a Letter
# Check the Letter has not Already Been Guessed
# Else - add to "guessed letters" list

# Letter by letter, check to see if the letter is in the word
# Update display word - print it
# if display_word = secret_word, break
# Loop }

# print congrats and amount of guesses