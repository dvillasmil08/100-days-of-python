# Instructions
# Make a rock, paper, scissors game.
#
# You'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.
#
# Start the game by asking the player:
#
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
#
# From there you will need to figure out:
#
# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
# You can find the "official" rules of the game on the World Rock Paper Scissors Association website.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gestures = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input >= 3 or user_input < 0:
    print("You typed an invalid number, you lose!")
else:
    print(gestures[user_input])

    computer_gesture = random.randint(0, 2)
    print(f"Computer chose:")
    print(gestures[computer_gesture])

    if user_input == 0 and computer_gesture == 2:
        print("You win!")
    elif computer_gesture == 0 and user_input == 2:
        print("You lose")
    elif computer_gesture > user_input:
        print("You lose")
    elif user_input > computer_gesture:
        print("You win!")
    elif computer_gesture == user_input:
        print("Its a draw")
