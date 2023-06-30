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

# Import the random module here
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Total items in list
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_to_pay = names[random_choice]
print(person_to_pay + " is going to buy the meal today.")
