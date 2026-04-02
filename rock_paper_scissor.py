# computer_choice="scissors"
import random

computer_choice=random.choice(["rock","paper","scissors"])

user_choice=input("Enter your choice: ")
print("Computer choice is :"+computer_choice+"\n")
if user_choice==computer_choice:
    print("TIE")
elif user_choice=="rock" and computer_choice=="scissors":
    print("YOU WIN")
elif user_choice=="paper" and computer_choice=="rock:":
    print("You win ")
elif user_choice=="scissors" and computer_choice=="paper":
    print("You win")
else:
    print("YOU LOSE")