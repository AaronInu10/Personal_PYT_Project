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

#Gets the user input
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")


#Creates a list for the computer to choose from
computer_input = [rock, paper, scissors]

#Allows the computer to pick randomly; selects list - computer_input. Remember index in list works like this - list_name [index]
computer_random = computer_input[random.randint(0,2)]

#draw condition
if user_input == computer_random:
  print (f"{computer_input[user_input]}It's a draw")

else:
#Prints computer choice
  computer_choice = print (f"Computer chooses: {computer_random}")

#if user chooses rock
  if user_input == "0":
    if computer_random == scissors:
      print (f"{rock}\nYou win!")
    elif computer_random == paper:
      print (f"{rock}\nYou lose!")

  #if user chooses paper
  elif user_input == "1":
    if computer_random == rock:
      print (f"{paper}\nYou win!")
    elif computer_random == scissors:
      print (f"{paper}\nYou lose!")

  #if user chooses scissors
  elif user_input == "2":
    if computer_random == paper:
      print (f"{scissors}\nYou win!")
    elif computer_random == rock:
      print (f"{scissors}\nYou lose!")

  #if they enter any number other than 0,1 or 2 - this comes out
  else:
    print ("You enter an invalid number. Please try again!")


  
