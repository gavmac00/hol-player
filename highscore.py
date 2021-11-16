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

score = 18
newHighScore(score)