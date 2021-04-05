from art import logo1
import random
from replit import clear
from art import goodbye
## Welcome line and GAME LOGO
print(logo1)
print("The answer will be a number betwen 1 and 100.")
# Generate the answer
# ANSWER = random.choice(range(1, 101))
# print(f"Code along with tested answer: {ANSWER}")
# Ask user to choose difficulty.
def set_game_level():
  level = input("Choose a difficulty level. Type 'easy', 'normal', or 'hard': ").lower()

  if level == 'easy':
    return 10
  elif level == 'normal':
    return 7
  elif level == 'hard':
    return 5
  else:
    print("input error, please choose again.")
    return set_game_level()


# design a function to show attempts left and let user guess:
def guessing():
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  return guess

# desing a function that take user's guess and compare to the ANSWER.
# if use answer inside below functions, remember to indicate it's global variable.
guess = 0
def compare():
  if guess < ANSWER:
    print("Too low.")
  elif guess > ANSWER:
    print("Too high.")

play = True
while play:
  ANSWER = random.choice(range(1, 101))
  attempts = set_game_level()
  while guess != ANSWER:
    guess = guessing()
    compare()
    attempts -= 1
    if attempts == 0:
      print("You've run out of guesses, you lose")
      print(f"The answer was: {ANSWER}")
      guess = ANSWER
    elif attempts > 0 and guess != ANSWER:
      print("Guess again.")

  ## If user got it right, jump out of the while loop and game ended.
  if attempts > 0:
    print(f"You got it! The answer was {ANSWER}.\n")
  play_again = input("Play again? Type 'y' or 'n': ").lower()
  if play_again == 'y':
    play = True
    clear()
    print(logo1)
  else:
    play = False

clear()
print(logo1)
print(goodbye)