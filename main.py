import random
from art import rock,paper,scissor

choice=[rock,paper,scissor]

computers_choice=random.randint(0,2)
print("Welcome To STONE PAPER SCISSOR GAME")
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

if user_choice>=3 or user_choice<0:  
  print("Invalid Choice, You Lose!")
else:
  user=choice[user_choice]
  computer=choice[computers_choice]
  print(user)
  print(f"Computer chooses:\n{computer}")

  if user==paper and computer==rock:
    print("You Won!")
  elif user==scissor and computer==paper:
    print("You Won!")
  elif user==rock and computer==scissor:
    print("You Won!")
  elif user==computer:
    print("Game Drawn")
  else:
    print("You lost")



