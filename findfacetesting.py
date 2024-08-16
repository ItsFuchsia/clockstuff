import random
letters = "ABSDEFRLINK"
sol = []
UL = 12
U = 12
UR = 12
L = 12
C = 12
R = 12
DL = 12
D = 12
DR = 12
BU = 12
BR = 12
BL = 12
BC = 12
BD = 12
#back moves defined by y2 NOT z2

#moveconvert
def mc(move, pair):
    return(letters.index(sol[move-1][pair-1]) + 1)

def randomletters():
    pair = letters[random.randint(0, len(letters))-1] + letters[random.randint(0, len(letters))-1]
    sol.append(pair)
    return(pair)

for i in range(7):
    randomletters()

print(sol)

#print((UL + mc(1, 2) + mc(2, 1) + mc(3, 1) + mc(4, 1) + mc(5, 1) + mc(6, 1) + mc(7, 1))% 12)

#print((U + mc(1, 2) + mc(2, 2) + mc(4, 1) + mc(5, 1) + mc(6, 1) + mc(7, 1)) % 12)

#print((UR + mc(1, 2) + mc(2, 2) + mc(3, 1) + mc(4, 2) + mc(5, 2) + mc(6, 2) + mc(7, 2)) %12)

#print((L + mc(1, 2) + mc(4, 1) + mc(5, 1) + mc(6, 1) + mc(7, 1)) % 12)

#print((C + mc(1, 2) + mc(2, 2) + mc(3, 2) + mc(4, 1) + mc(5, 1) + mc(6, 1) + mc(7, 1)) % 12)

#print((R + mc(1, 2) + mc(2, 2) + mc(3, 2) + mc(4, 1) + mc(7, 1)) % 12)

#print((DL + mc(1, 1) + mc(2, 1) + mc(3, 1) + mc(4, 2) + mc(5, 2) + mc(6, 1) + mc(7, 1)) % 12)

#print((D + mc(1, 2) + mc(2, 2) + mc(3, 2) + mc(4, 1) + mc(6, 1) + mc(7, 1)) % 12)

#print((DR + mc(1, 2) + mc(2, 2) + mc(3, 2) + mc(4, 1) + mc(5, 2) + mc(6, 2) + mc(7, 1)) % 12)

#print((BU - mc(2, 1) - mc(3, 1) - mc(4, 2) - mc(5, 2) - mc(6, 2) - mc(7, 2)) %12)

#print((BR - mc(1, 1) - mc(2, 1) - mc(3, 1) - mc(4, 2) - mc(5, 2)) % 12)

#print((BL - mc(3, 1) - mc(4, 2) - mc(5, 2) - mc(6, 2) - mc(7, 2)) % 12)

#print((BC - mc(1, 1) - mc(2, 1) - mc(3, 1) - mc(4, 2) - mc(5, 2) - mc(6, 2) - mc(7, 2))%12)

print((BD - mc(1, 1) - mc(2, 1) - mc(3, 1) - mc(4, 2) - mc(5, 2) - mc(6, 2)) %12)