import random
import time
letters = "ABSDEFRLINK"
timedelay = 2

def randomletters():
    return(letters[random.randint(0, len(letters))-1] + letters[random.randint(0, len(letters))-1])

while True:
    for i in range(7):
        print(randomletters())
        time.sleep(timedelay)
    print("solution done, restarting")
    if timedelay >= 0.5:
        timedelay -= 0.1
    time.sleep(2)