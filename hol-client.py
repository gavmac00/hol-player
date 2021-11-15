#version 2.1 of higher or lower game - Gavin MacDonnell 14/11/21

#this file contains base code for the original higher or lower 2 game,
# but modifications have been made such that it works
# alongside hol-player.py (an autonomous player)

import random as random
import time
#instructions
print("\n\nA game of Higher or Lower. Each round, press 'h' for \"Higher\", press 'l' for \"Lower\".")

status = 1 #the current player status (playing = 1, lost = 0)
score = 0 #rounds completed 

#starting number is displayed to user & written in hol-data.txt
old = random.randint(1,100)
print("The starting number is " + str(old))


give = "new: " + str(old) + "\nend"
with open('hol-data.txt', 'w') as wd:
    wd.write(give)
    wd.close()

#prompts for higher or lower
print("Higher or Lower? ") #changed input to print here (so as to not hold up the console)

time. sleep(5)

with open('hol-data.txt', 'r') as rd:
    has_been_changed = rd.read()
    rd.close()

print(has_been_changed)

if  has_been_changed[1] == "v":
    print("indexing correct")
else:
    print("indexing incorrect")

# while status == 1:
#     new = random.randint(1,100)
#     print("\n")
#     if choice == "h":
#         if new > old:
#             print(str(new) + " is higher than " + str(old) + ".")
#             score = score + 1
#         else: 
#             print(str(new) + " is not higher than " + str(old) + ".")
#             status = 0
#             print("Game over, Score: " + str(score))
#             break

#     if choice == "l":
#         if new < old:
#             print(str(new) + " is lower than " + str(old) + ".")
#             score = score + 1
#         else:
#             print(str(new) + " is not lower than " + str(old) + ".")
#             status = 0
#             print("Game over, Score: " + str(score))            
#             break
#     choice = input("Higher or Lower? ")
#     old = new