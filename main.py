import random
import time

print("--- BR Orel Reshka ---")

user = input("Type ""X"" to start the game: ")

if user == "X":
    x = random.randint(1, 2)
    print("The game has begun")
    if x == 1:
        time.sleep(2)
        print("THE EAGLE FELL OUT")
    elif x == 2:
        time.sleep(2)
        print("THE TAIL FELL OUT")
else:
    print("WRONG LETTER")

