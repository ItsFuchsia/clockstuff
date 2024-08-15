import random
import time
letters = "ABSDEFRLINK"


while True:
    print(letters[random.randint(0, len(letters))-1] + letters[random.randint(0, len(letters))-1])
    time.sleep(1.5)