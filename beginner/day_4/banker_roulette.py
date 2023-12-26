import random

names_string = input("Who all are coming to Dinner? Enter the names separated by a comma\n")

names_list = names_string.split(", ")
people = len(names_list)
name_pick = names_list[random.randint(0, people)]
print(f"{name_pick} is paying tonight!")

