import random
import time
letters = "ABSDEFRLINK"

def randomletters():
    return(letters[random.randint(0, len(letters))-1] + letters[random.randint(0, len(letters))-1])

while True:
    for i in range(7):
        print(randomletters())
        time.sleep(1.5)
    print("solution done, restarting")
    time.sleep(2)