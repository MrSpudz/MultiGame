from random import randint
from os import path, system
import webbrowser as wb
from time import sleep


# Log Relative Path Setup
absolutePath = path.dirname(__file__)
logRelPath = "../logs/"
logFullPath = path.join(absolutePath, logRelPath)

# Main Relative Path Setup
absolutePath = path.dirname(__file__)
relPath = "../gameFiles/"
fullPath = path.join(absolutePath, relPath)

# Admin Relative Path Setup
adminAbsolutePath = path.dirname(__file__)
adminRelPath = "../main/admin/"
adminFullPath = path.join(absolutePath, relPath)


def clear():
    system('clear')


def endLog():
    fish = randint(0, 3)
    f = open(logFullPath + "game.log", "a")
    if fish != 0:
        f.write("END OF LOG FILE!")
    else:
        f.write("END OF LOG FILE! So long and thanks for all the fish!")
    f.close()
    quit()


def menu():
    with open(absolutePath=path.dirname(__file__) + "../main/start.py") as f:
        exec(f.read())


clear()

exit = 0
exitAdmin = 0

print("GAMES:")
print("1: Guess the Number")
print("2: Rock Paper Scissors")
print("3: Hangman (WIP)")
print("4: Admin Tools")

print("QUIT Game (any key)")

game = input("What game would you like to play? ")

if game == "1":  # Opens Guess the Number
    with open(path.dirname(__file__) + "/../gameFiles/GTN/GuessTheNum.py") as f:
        exec(f.read())
        quit()
elif game == "2":  # Opens Rock Paper Scissors
    with open(path.dirname(__file__) + "/../gameFiles/RPS/RockPaperScissors.py") as f:
        exec(f.read())
        quit()
elif game == "3":  # Opens Hangman
    with open(path.dirname(__file__) + "/../gameFiles/Hangman/Hangman.py") as f:
        exec(f.read())
        quit()
elif game == "4":
    with open(adminFullPath + "/../main/admin/admin.py") as f:
        exec(f.read())
        quit()
else:
    endLog()

quit()
