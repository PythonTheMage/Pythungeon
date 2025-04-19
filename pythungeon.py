import random
import os

print("WELCOME TO THE PYTHUNGEON")
def main():
    
    main.misinput = 0
    menu()

def start():
    os.system('cls')
    print("~THE PYTHUNGEON~")
    print("It took a lifetime, but you've finally found it.\nThe Legendary Pythungeon.")
    print("A tall stone door seemlessly fits into the mountainside.")
    print("This place is easy to miss for those who aren't looking for it.")
    print("\nDanger waits around every corner, and you may not return.")
    print("Nonetheless, you find your resolve, force open the door, and delve into the Pythungeon...")
    input()
    pass

def menu():
    print("\x1B[3mENTER\x1B[0m if you dare! ")

    selection = input("")
    if selection.lower() == "quit":
        quit()
    elif main.misinput == 3:
        os.system('cls')
        print("type 'enter' or 'quit'")
        main.misinput = 0
        menu()
    elif selection.lower() != "enter":
        print("You must not have heard me correctly... *loudly clears throat*")
        main.misinput += 1
        menu()
    else:
        start()

main()