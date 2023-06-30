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
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")


