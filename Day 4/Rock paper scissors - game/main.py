import random
import my_ascii

# RULES of the game
# Rock crushes scissors, scissors cut paper, and paper covers rock

while(True):

  user_choice = input("Enter your choice R for rock, P for paper or S for scissors :")
  
  if user_choice.casefold() == "r":
    print(my_ascii.rock)
  elif user_choice.casefold() == "p":
    print(my_ascii.paper)
  elif user_choice.casefold() == "s":
    print(my_ascii.scissors)
  else:
    print("You did not enter a valid choice")
  
  random_number = random.randint(0,2)
  
  computer_options = ["R", "P", "S"]
  
  print("Computer chose:")
  if random_number == 0:
    print(my_ascii.rock)
  elif random_number == 1:
    print(my_ascii.paper)
  elif random_number == 2:
    print(my_ascii.scissors)
  
  if  random_number == 0: # R
    if user_choice.casefold() == "r":
      print("draw")
    elif  user_choice.casefold() == "p":
      print("Computer wins")
    elif user_choice.casefold() == "s":
      print("You win")
  elif random_number == 1: # P
    if user_choice.casefold() == "r":
      print("You win")
    elif  user_choice.casefold() == "p":
      print("Draw")
    elif user_choice.casefold() == "s":
      print("Computer wins")
  elif random_number == 2: # S
    if user_choice.casefold() == "r":
      print("You win")
    elif  user_choice.casefold() == "p":
      print("You lose")
    elif user_choice.casefold() == "s":
      print("Draw")
      