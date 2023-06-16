import random

# Generate a random number between 1 and 50
guess_range = 50
answer = random.randint(1, guess_range)

# Start the game and ask the player to guess the number
print('Welcome to the number guessing game!')
print('')
user_input = input(f"Guess a number between 1 and {guess_range} : \n")
guess = int(user_input)