import random as random
import time
from threading import Thread

def client():
    loss = "--------------"
    status = 1
    score = 1
    old = random.randint(1,100)
    give = "new: " + str(old) + "\nend"

    #instructions
    print("\n\nA game of Higher or Lower. Each round, press 'h' for \"Higher\", press 'l' for \"Lower\".")
    print("The starting number is " + str(old))

    with open('hol-data.txt', 'w') as wd:
        wd.write(give)
        wd.close()

    print("Higher or Lower?")
    time. sleep(8)

    while status == 1:
        #read phase
        with open('hol-data.txt', 'r') as rd:
            vote = rd.read()
            rd.close()

        while vote[0] == "v":
            time.sleep(1)
            choice = vote[6]
            print("Client interpreted: " + choice + ".")

            #descision phase
            new = random.randint(1,100) 

            if choice == "h":
                if new > old:
                    print(str(new) + " is higher than " + str(old) + ".")
                    score = score + 1
                    old = new
                else: 
                    status = 0
                    print(str(new) + " is not higher than " + str(old) + ".")
                    with open('hol-data.txt', 'w') as ld:
                        ld.write(loss)
                        ld.close()
                        time.sleep(2)
            if choice == "l":
                if new < old:
                    print(str(new) + " is lower than " + str(old) + ".")
                    score = score + 1
                    old = new
                else:
                    status = 0
                    print(str(new) + " is not lower than " + str(old) + ".")
                    with open('hol-data.txt', 'w') as ld:
                        ld.write(loss)
                        ld.close()
                        time.sleep(2)

            print("Round: " + str(score))

            #new round phase
            if status == 1:
                give = "new: " + str(old) + "\nend"
                with open('hol-data.txt', 'w') as wd:
                    wd.write(give)
                    wd.close()
                    print("Now, Higher or Lower? ")
                time.sleep(8)
            else:
                break

        vote = give
        time.sleep(1)
                    
    #loss
    print("Game over, Score: " + str(score))
    time.sleep(4)
    quit()

def player():
    new = "vote: h\nend"
    alltext = "vote: h\nend"
    time.sleep(2) #starts at 4 seconds

    while not alltext[0] == "-":

        with open('hol-data.txt') as rd:
            alltext = rd.read()

        while alltext[5].isdigit():
            time.sleep(1)
            new_u = alltext[5] #units
            new = new_u

            new_t = alltext[6] #tens
            new_h = alltext[7] #hundreds

            if new_t.isdigit():
                new = new_u + new_t

            if new_h.isdigit():
                new = new_u + new_t + new_h
                        
            new = int(new)
            print("     Player interpreted: " + str(new) +".")

            #voting phase
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

            send = "vote: " + vote + "\nend"

            with open('hol-data.txt', 'w') as wd:
                wd.write(send)
                wd.close()
                print("     Player cast vote of: " + vote)

            time.sleep(8)
            alltext = send
            time.sleep(1)
            
    print("     Player undestood a loss.")
    quit()

Thread(target = client).start()
Thread(target = player).start() 


