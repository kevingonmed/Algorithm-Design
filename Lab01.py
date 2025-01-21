# 1. Name: 
#    Kevin Gonzalez
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#   The program is a guessing game. In the first part, the program will ask for an integer, and then it will select a random number between 1 and the integer you provide. After that, the program will ask you to guess numbers and give hints if your guess is too high or too low. While doing this, the program will keep track of the number of attempts and store all the numbers you've guessed until you find the correct answer.
# 4. What was the hardest part? Be as specific as possible.
#    I think the hardest part for me was that I was a little rusty with my Python skills, and I had to read a bit to remember how to apply the if statement and the while loop. When I first wrote the code, I didn’t know the correct syntax for the loops, but after reviewing it, it became much easier to implement. Another challenge was working with the guesses array and figuring out how to add values to it. I completely forgot about the .append() command, and at first, I placed it outside the loop. Once I corrected that, the implementation was much smoother.
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program- 
#   I spend 4 hours.  

import random


# Game introduction.
# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Pick a positive integer: "))

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print("This is the 'guess a number' game.")
print("You try to guess a random number in the smallest number of attempts.")

# Initialize the sentinal and the array of guesses.
guesses = []

# Play the guessing game.
while True:
    # Prompt the user for a number.
    print(f"Guess a number between 1 and {value_max}: ")
    guess = int(input())  # Capture the user's guess
    
    # Store the guess in the array so it can be displayed later.
    guesses.append(guess)
    
    # Make a decision: was the guess too high, too low, or just right.
    if guess < value_random:
        print("Your guess was too low.")
    elif guess > value_random:
        print("Your guess was too high.")
    else: 
        print("You got it!")
        break

# Give the user a report: How many guesses and what the guesses were.
print(f"You got it in {len(guesses)} guesses.")
print(f"The guesses were: {guesses}")
