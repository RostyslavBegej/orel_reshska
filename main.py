import random
import time

print("--- BR Orel Reshka ---")

while True:
    user = input("Type 'x' to start the game: ")
    if user == "x":
        x = random.randint(1, 2)
        print("The game has begun...")
        if x == 1:
            time.sleep(1)
            print("THE EAGLE FELL OUT🦅")
        elif x == 2:
            time.sleep(1)
            print("THE TAIL FELL OUT🐈")
    else:
        print("WRONG LETTER!")
input()
