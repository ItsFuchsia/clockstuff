import random
import time
letters = "ABSDEFRLINK"
timedelay = float(input("Start delay between moves (s)? \n"))
enddelay = float(input("final delay between moves (s) ? \n"))
speedup = 0.1
sol = []

state = {
    "UL": 12,
    "U" : 12,
    "UR" : 12,
    "L" : 12,
    "C" : 12,
    "R" : 12,
    "DL" : 12,
    "D" : 12,
    "DR" : 12,
    "BU" : 12,
    "BR" : 12,
    "BL" : 12,
    "BC" : 12,
    "BD" : 12 }

movelookup = {
    "UL": [2, 1, 1, 1, 1, 1, 1],
    "U":  [2, 2, 0, 1, 1, 1, 1],
    "UR": [2, 2, 1, 2, 2, 2, 2],
    "L":  [2, 0, 0, 1, 1, 1, 1],
    "C":  [2, 2, 2, 1, 1, 1, 1],
    "R":  [2, 2, 2, 1, 0, 0, 1],
    "DL": [1, 1, 1, 2, 2, 1, 1],
    "D" : [2, 2, 2, 1, 0, 1, 1],
    "DR": [2, 2, 2, 1, 2, 2, 1],
    "BU": [0, 1, 1, 2, 2, 2, 2],
    "BR": [1, 1, 1, 2, 2, 0, 0],
    "BL": [0, 0, 1, 2, 2, 2, 2],
    "BC": [1, 1, 1, 2, 2, 2, 2],
    "BD": [1, 1, 1, 2, 2, 2, 0]
}

def p(clock, inv = 1):
    s = str(inv*state[clock]%12)
    return " "*(2-len(s)) + s


def printstate():
    for key in movelookup:
        for i, j in enumerate(movelookup[key]):
            if key.startswith("B"):
                state[key] -= mc(i + 1, j)
            else:
                state[key] += mc(i + 1, j)
    print(p("UL") + ", " + p("U") + ", " + p("UR") + "\t" + p("UR", -1) + ", " + p("BU") + ", " + p("UL", -1))
    print(p("L") + ", " + p("C") + ", " + p("R") + "\t" + p("BL") + ", " + p("BC") + ", " + p("BR"))
    print(p("DL") + ", " + p("D") + ", " + p("DR") + "\t" + p("DR", -1) + ", " + p("BD") + ", " + p("DL", -1))

def mc(move, pair):
    if pair == 0:
        return(0)
    #print(str(move) + "\n" + str(pair))
    return(letters.index(sol[move-1][pair-1]) + 1)



def randomletters():
    pair = letters[random.randint(0, len(letters))-1] + letters[random.randint(0, len(letters))-1]
    return(pair)

while True:
    for i in range(7):
        sol.append(randomletters())
    for i in sol:
        print(i)
        time.sleep(timedelay)
    printstate()
    success = "y" in input("Did that work? \n")
    if success:
        if timedelay > enddelay:
            timedelay -= speedup
        print("solution done, restarting, new time interval: " + str(round(timedelay, 1)))
    else:
        print(sol)
        exit()
    sol = []
    time.sleep(2)