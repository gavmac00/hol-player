from threading import Thread
import random as random
import time

def client():
    loss = "--------------"
    status = 1
    score = 1
    old = random.randint(1,100)
    give = "new: " + str(old) + " end"
    vote = "nresetforsafety"

    clientBegin(give,score,old)
    time.sleep(10)

    while status == 1:
        if vote[0] == "n":
            vote = clientRead()
            choice = vote[6]

        new = random.randint(1,100) 
        #print("A: choice: " + choice + ", new: " + str(new) + ", old: " + str(old))
        status = clientStatusResponse(choice,new,old) #status decided here

        clientOutput(status,choice,new,old,loss) # "X was higher/lower than Y..."
        vote = "nresetforsafety"
        #next round
        if status == 1:
            score = score + 1
            old = new
            print("\nRound: " + str(score))
            give = "new: " + str(old) + " end"
            with open('hol-data.txt', 'w') as wd:
                wd.write(give)
                print("Now, Higher or Lower? ")
            time.sleep(10)
        else:
            clientWriteLoss(loss)
    
    #loss
    print("\nGame over, Score: " + str(score))
    newHighScore(score)
    time.sleep(5)
    quit()

def player():
    time.sleep(5)
    new = "vote: h\ end"
    alltext = "vote: h\ end"

    while not alltext[0] == "-": #status = 1
        alltext = playerRead()
        #print("1: " + alltext)
        if alltext[0] == "v":
            alltext = playerRead()
            print("2: " + alltext)
            time.sleep(0.5)
        if alltext[5].isdigit():
            new = playerAppend(alltext)
            send = playerVote(new)
            with open('hol-data.txt', 'w') as wd:
                wd.write(send)
            time.sleep(10)
            alltext = "resetforsafety"
        else:
            break
    #status = 0
    quit()

def clientBegin(give,score,old):
    print("\n\nA Game of Higher or Lower.")
    print("Each round, press 'h' for \"Higher\", press 'l' for \"Lower\".")

    with open('hol-data.txt', 'w') as wd:
        wd.write(give)

    print("\nRound: " + str(score) + ", The starting number is " + str(old))
    print("Higher or Lower?")

def clientStatusResponse(choice,new,old):
    if choice == "h":
        if new > old:
            status = 1
        else: 
            status = 0
    if choice == "l":
        if new < old:
            status = 1
        else:
            status = 0
    return status

def clientWriteLoss(loss):
    with open('hol-data.txt', 'w') as ld:
        ld.write(loss)
    
def clientRead():
    with open('hol-data.txt', 'r') as rd:
        vote = rd.read() 
    return vote 

def clientOutput(status,choice,new,old,loss):
    if choice == "h":
        if status == 1:
            print(str(new) + " is higher than " + str(old) + ".")
        else: 
            print(str(new) + " is not higher than " + str(old) + ".")
            clientWriteLoss(loss)
    if choice == "l":
        if status == 1:
            print(str(new) + " is lower than " + str(old) + ".")
        else:
            print(str(new) + " is not lower than " + str(old) + ".")
            clientWriteLoss(loss)

def playerAppend(alltext):
    new_u = alltext[5] #units
    new = new_u

    new_t = alltext[6] #tens
    new_h = alltext[7] #hundreds

    if new_t.isdigit():
        new = new_u + new_t

    if new_h.isdigit():
        new = new_u + new_t + new_h
                
    new = int(new)
    return new

def contemplate():
    rando = random.randint(1,20)
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

def playerRead():
    with open('hol-data.txt') as rd:
        alltext = rd.read()
    return alltext

def newHighScore(score):
    with open('highscore.txt', 'r') as rd:
        oldHighScore = rd.read()

    oldHighScore = highScoreAppend(oldHighScore)

    if score > oldHighScore:
        newHighScore = "High Score: " + str(score) + " end"
        with open('highscore.txt', 'w') as hd:
            hd.write(newHighScore)

def highScoreAppend(oldHighScore):

    new_u = oldHighScore[11] #units
    new = new_u

    new_t = oldHighScore[12] #tens
    new_h = oldHighScore[13] #hundreds

    if new_t.isdigit():
        new = new_u + new_t

    if new_h.isdigit():
        new = new_u + new_t + new_h
                
    new = int(new)
    return new

Thread(target = client).start()
Thread(target = player).start()