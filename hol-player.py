# this python script is created with the intention of it playing the higher
# or lower game automomously, lets see how it goes - Gavin MacDonnell 14/11/21

import random as random

#read the text file
with open('hol-data.txt') as rd:
    alltext = rd.read()

#do something with the information
new_u = alltext[5] #units
new_t = alltext[6] #tens
new_h = alltext[7] #hundred (if == 100)

new = new_u

#append the charachters
if new_t.isdigit():
    new = new_u + new_t

if new_h.isdigit():
    new = new_u + new_t + new_h

print("new: " + new)

new = int(new) #at this point, player knows what the new value is

#now to enter whether we want to guess higher or lower
h = "h"
l = "l"

if new < 50:
    vote = h

elif new > 50:
    vote = l

else:
    pr = random.randint(1,2)
    if pr == 1:
        vote = h
    else:
        vote = l

#at this point, vote is chosen
send = "vote: " + vote
with open('hol-data.txt', 'w') as wd:
    wd.write(send) # vote is sent, now on to the client