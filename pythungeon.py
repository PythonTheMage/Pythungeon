import random

print("Welcome to the Pythungeon!")
print("Now being used as a sandbox for rpg combat")

STR = 2

while True:
    input("Press Enter")

    mSTR = STR+5
    AP = random.randint(STR,mSTR)
    print(AP)