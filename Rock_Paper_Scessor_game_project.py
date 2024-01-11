import random
import sys

while True:
 try:
    Rock = """-------Rock--------------"""
    Paper = """-------Paper------------"""
    Scessor = """-------Scessor--------"""
    game_image = [Rock,Paper,Scessor]
    uesr_choice = int(input("enter your choice: type 0 for Rock, 1 for Paper, 2 for Scessor: "))
    print(game_image[uesr_choice])
    computer_choice = random.randint(0, 2)
    print("computer_choice:")
    print(game_image[computer_choice])
    if uesr_choice >= 3 or uesr_choice < 0:
     print("Please enter the number between Zero to Two: ")
     continue
    if uesr_choice == 'e':
        break
    if computer_choice == uesr_choice:
        print("Drawn")
    elif computer_choice ==0 and uesr_choice == 2:
        print("You Loss")
    elif computer_choice ==2 and uesr_choice == 0:
        print("You Win")
    elif uesr_choice > computer_choice: #2>0
        print("You Win")
    elif computer_choice > uesr_choice: #2>0
            print("You Loss")
 except:
      sys.exit()

print("Invalid Choice")





