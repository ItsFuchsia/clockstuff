import random
letters = "ABSDEFRLINK"
sol = []
UL = 12


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

print((UL + mc(1, 2) + mc(2, 1) + mc(3, 1) + mc(4, 1) + mc(5, 1) + mc(6, 1) + mc(7, 1))% 12)