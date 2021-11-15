# this python script is created with the intention of it playing the higher
# or lower game automomously, lets see how it goes - Gavin MacDonnell 14/11/21

import random as random
import time

def player():
    time.sleep(4)
    new = "v"
    while not new.isdigit(): # leaves this loop only when correct data is present
        #read the text file
        with open('hol-data.txt') as rd:
            alltext = rd.read()

        #do something with the information
        new_u = alltext[5] #units
        new = new_u

        new_t = alltext[6] #tens
        new_h = alltext[7] #hundred (if == 100)

        #append the charachters
        if new_t.isdigit():
            new = new_u + new_t

        if new_h.isdigit():
            new = new_u + new_t + new_h
                
    new = int(new) #at this point, the string is certain it can be a digit, simply assigning it here and now the player knows what the 'new' value is

    while not alltext[0] == "-":
        new = "v"
        #read the text file
        with open('hol-data.txt') as rd:
            alltext = rd.read()

        #do something with the information
        new_u = alltext[5] #units
        new = new_u

        new_t = alltext[6] #tens
        #new_h = alltext[7] #hundred (if == 100)

        #append the charachters
        if new_t.isdigit():
            new = new_u + new_t

        if new_h.isdigit():
            new = new_u + new_t + new_h
        
        new = int(new) #at this point, the string is certain it can be a digit, simply assigning it here and now the player knows what the 'new' value is
        print("     Player understood 'new' value as: " + str(new) +".")

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
            wd.write(send)
            wd.close()
        
        print("     Player cast vote of: " + vote) # vote is sent, now on to the client
        time.sleep(8)

        with open('hol-data.txt') as rd:
            alltext = rd.read()
        new = str(new)

    quit()