import random
roll=random.randint(1,6)
user_number=int(input("Guess the number\n"))
if user_number==roll:
    print("You guessed right. They rolled at"+str(roll))
else:
    print("You guessed wrong. They rolled at"+str(roll))