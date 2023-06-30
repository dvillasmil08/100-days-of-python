# import random
#
# coin_flip = random.randint(0, 1)
#
# if coin_flip == 1:
#     print("Heads")
# else:
#     print("Tails")
#
# List
# fruits = [item1, item2]

import random
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# # Total items in list
# num_items = len(names)
#
# random_choice = random.randint(0, num_items - 1)
# person_to_pay = names[random_choice]

# With random.choice
# person_to_pay = random.choice(names)
# print(person_to_pay + " is going to buy the meal today.")

# Nested Lists

# Treasure map
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# map[vertical - 1][horizontal -1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")
#
#
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
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
gestures = [rock, paper, scissors]
print(gestures[user_input - 1])

