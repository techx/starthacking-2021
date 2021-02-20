import random

# ignore the line of code below, but keep it
random.seed()

# Taking inputs to establish range 
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

# Generating random number between the lower and upper
random_number = random.randint(lower, upper)

# Initializing the number of guesses.
count = 0

# Initialize variable for last guess
guess = None

# For calculation of minimum number of guesses depends upon range
while guess != random_number:
  # Taking guessed number as input
  guess = int(input("Guess a number: "))

  # Condition testing
  if random_number > guess:
    print("You guessed too small!")
  elif random_number < guess:
    print("You Guessed too high!")
  
  count += 1


print("Congratulations you did it in", count, "tries")

