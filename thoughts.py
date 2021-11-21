# random thoughts for higher-or-lower Ai.
# Gavin MacDonnell 20/11/21.

import random as random

def contemplate():
    rando = random.randint(1,10)
    print(rando)
    if rando == 1:
        thought = 1
    else:
        thought = 0
    return thought

def playerVote(new):
    h = "h"
    l = "l"
    t = contemplate()

    if t == 0:
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
    
    else:
        if new < 50:
            vote = l

        elif new > 50:
            vote = h

        else:
            pr = random.randint(1,2)
            if pr == 1:
                vote = l
            else:
                vote = h

    send = "vote: " + vote + " end"
    print("     Player Votes: " + vote)
    return send

new = 44
vote = playerVote(new)
print("Vote: " + vote)