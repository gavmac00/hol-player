#copy of version 2 of higher or lower game - Gavin MacDonnell 14/11/21

import random as random

#instructions
print("\n\nA game of Higher or Lower. Each round, press 'h' for \"Higher\", press 'l' for \"Lower\".")

status = 1 #the current player status (playing = 1, lost = 0)
score = 0 #rounds completed 

#starting number is displayed to user
old = random.randint(1,100)
print("The starting number is " + str(old))

#prompts for higher or lower
choice = input("Higher or Lower? ")

while status == 1:
    new = random.randint(1,100)
    print("\n")
    if choice == "h":
        if new > old:
            print(str(new) + " is higher than " + str(old) + ".")
            score = score + 1
        else: 
            print(str(new) + " is not higher than " + str(old) + ".")
            status = 0
            print("Game over, Score: " + str(score))
            break

    if choice == "l":
        if new < old:
            print(str(new) + " is lower than " + str(old) + ".")
            score = score + 1
        else:
            print(str(new) + " is not lower than " + str(old) + ".")
            status = 0
            print("Game over, Score: " + str(score))            
            break
    choice = input("Higher or Lower? ")
    old = new