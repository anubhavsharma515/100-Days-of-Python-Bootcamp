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

choices = [rock, paper, scissors]
num_choices = len(choices) - 1

print("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors")

choice = int(input())
computer_choice = random.randint(0, num_choices)

print(f"You chose: \n {choices[choice]}")
print(f"Computer chose: \n {choices[computer_choice]}")

if choice == computer_choice:
  print("It's a tie!")
elif choice == computer_choice+1:
  print("Computer wins")
elif choice == 0 and computer_choice == 2:
  print("You win")
else:
  print("Computer wins")
