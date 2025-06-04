import random

# Generates a random number
print("Guess My Number")
secret_number = random.randint(1, 100)
print(secret_number)
# Creates Counter Variable
counter = 0

# Loop
while True:
    guess = int(input("Guess a Number: "))
    print(guess)
    counter += 1
    if guess > secret_number:
        print("Guess Too High")
    elif guess < secret_number:
        print("Guess Too Low")
    else:
        break
# Correct Answer & Congratulations
print("Correct!")
print(f"You Guessed the number in {counter} guesses.")



# haiii

# start loop
#   prompt user to guess number
#   recieve user's input, save as num
#   increment counter variable to 0
#   if guess >num, too high
#   if guess <num, too low
#   if guess =num, correct & end loop

# tell user the state of counter variable

#i made this :D