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

#Write your code below this line 👇
import random

user_choice = int(
    input(
        "please enter your choise 0 for rocks, 1 for paper and 2 for scissoes : "
    ))
if user_choice >= 3 or user_choice < 0:
    print("You have typed a invalid number you loose...")
elif user_choice == 0:
    print(f"you choose {rock}")
elif user_choice == 1:
    print(f"you choose {paper}")
elif user_choice == 2:
    print(f"you choose {scissors}")

set = [[rock], [paper], [scissors]]
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(f"computer chooses {rock}")
elif computer_choice == 1:
    print(f"computer chooses {paper}")
elif computer_choice == 2:
    print(f"computer chooses {scissors}")
print(computer_choice)

if user_choice == 0 and computer_choice == 2:
    print("you loose...")

elif user_choice == 0 and computer_choice == 1:
    print("you won...")

elif user_choice == computer_choice:
    print("its a tie please try again...")

if user_choice == 1 and computer_choice == 0:
    print("you loose....")

elif user_choice == 1 and computer_choice == 2:
    print("you won...")

if user_choice == 2 and computer_choice == 0:
    print("you loose...")

elif user_choice == 2 and computer_choice == 1:
    print("you won...")

print("thanks for playing please come back again.......")