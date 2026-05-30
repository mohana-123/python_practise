# Number Guessing Game
'''
## Description:
A simple Python game where the program generates a random number and the user has to guess it.

## Features:
- Random number generation
- User input
- Feedback (Too high / Too low)
- Loop until correct guess

## Concepts Used:
- Python basics
- Loops
- Conditionals
- Random module
'''

import random

chances = 0
random_num = random.randint(1,100)
print(random_num)
print("You are given 7 chances to guess the number")

while chances < 7:
    user_input = int(input("Guess the number! => "))
    chances +=1
    if chances >= 7:
        print(f"you didn't guessed it. The number is {random_num}")
        break
    if user_input < random_num:
        print(f"Too low, you have used {chances} chances out of 7 to guess")
    elif user_input > random_num:
        print(f"Too high, you have used {chances} chances out of 7 to guess")
    else:
        print(f"you have guess it right! The number is {random_num}")
        print(f"You took {chances} chances out of 7 to guess. Congrats!")
        break
