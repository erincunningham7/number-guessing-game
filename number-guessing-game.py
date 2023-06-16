
import random

# Keep track of the players number of guesses allowed
guesses_allowed = 10

# Generate a random number between 1 and 50
guess_range = 50
answer = random.randint(1, guess_range)

# Start the game and ask the player to guess the number
print('Welcome to the number guessing game!')
print('')
user_input = input(f"Guess a number between 1 and {guess_range} : \n")
guess = int(user_input)

# Compare the users input to the random number generated and check if it matches
# If statement that only repeats a limited amount of guesses
for i in range(guesses_allowed):
    user_input = input(f"Guess a number between 1 and {guess_range} : \n")
    guess = int(user_input)
    # If the guess is correct break out of the loop
    if guess == answer:
        print('Congratulations! You guessed the correct number. You win!')
        break
    # Add hints
    elif guess < answer:
        print('The number is higher.')
    else:
        print('The number is lower.')
    # Check if the player has reached their number of guesses limit and end the game if so
    if (i == guesses_allowed -1):
        print('Sorry, you have run out of guesses. You lose!')
    # Add additional hints
    if abs(guess - answer) <= 10:
        print("You're warm!")
    elif abs(guess-answer) <= 20:
        print("You're getting warmer!")
    elif abs(guess - answer) <= 30:
        print("You're cold.")
    else:
        print("You're freezing.")

# If the code executes past the while loop the user has guessed the correct answer
# print('Congratulations! You guessed the correct number. You win!')

