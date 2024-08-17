import random
import numpy as np

letters = "ABSDEFRLINK"
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
#back moves defined by y2 NOT z2

#moveconvert
def mc(move, pair):
    if pair == 0:
        return(0)
    #print(str(move) + "\n" + str(pair))
    return(letters.index(sol[move-1][pair-1]) + 1)

def randomletters():
    pair = letters[random.randint(0, len(letters))-1] + letters[random.randint(0, len(letters))-1]
    sol.append(pair)
    return(pair)

for i in range(7):
    randomletters()

print(sol)


dic = {
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

for key in dic:
    for i, j in enumerate(dic[key]):
        if key.startswith("B"):
            state[key] -= mc(i + 1, j)
        else:
            state[key] += mc(i + 1, j)

def p(clock, inv = 1):
    s = str(inv*state[clock]%12)
    return " "*(2-len(s)) + s

print(p("UL") + ", " + p("U") + ", " + p("UR") + "\t" + p("UR", -1) + ", " + p("BU") + ", " + p("UL", -1))
print(p("L") + ", " + p("C") + ", " + p("R") + "\t" + p("BL") + ", " + p("BC") + ", " + p("BR"))
print(p("DL") + ", " + p("D") + ", " + p("DR") + "\t" + p("DR", -1) + ", " + p("BD") + ", " + p("DL", -1))