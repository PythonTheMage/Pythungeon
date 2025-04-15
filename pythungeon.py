import random

print("RPG COMBAT SIMULATION")


STR = 2

while True:
    input("Press Enter")

    mSTR = STR+5
    AP = random.randint(STR,mSTR)
    print(AP)