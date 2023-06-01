import random

active_player = "Player1"
run = True

def conversion(number):
    if number == 1:
        return "Schere"
    elif number == 2:
        return "Stein"
    elif number == 3:
        return "Papier"

choise = input("Drücke die 1 für die Schere, die 2 für den Stein und die 3 für das Papier: ")
choise = int(choise)
print(conversion(choise))

computer = random.randint(1, 3)
if computer == 1:
    wahl = "Schere"
elif computer == 2:
    wahl = "Stein"
elif computer == 3:
    wahl = "Papier"

if computer == choise:
        print("Es ist ein Unentschieden")
else:
    if choise == 1:
        if computer == 2:
            print("Du hast verloren.")
        elif computer == 3:
            print("Du hast gewonnen.")
    if choise == 2:
        if computer == 3:
            print("Du hast verloren.")
        elif computer == 1:
            print("Du hast gewonnen.")
    if choise == 3:
        if computer == 3:
                print("Du hast verloren.")
        elif computer == 1:
                print("Du hast gewonnen.")


