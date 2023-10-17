# init
from random import randint
from os import system,path
from time import sleep

# Log Relative Path Setup
absolutePath = path.dirname(__file__)
logRelPath = "../logs/"
logFullPath = path.join(absolutePath, logRelPath)

# Main Relative Path Setup
absolutePath = path.dirname(__file__)
relPath = "../main/"
fullPath = path.join(absolutePath, relPath)


def menu():
    with open(fullPath + "start.py") as f:
        exec(f.read())


def logData():
    f = open(logFullPath + "game.log", "a")
    f.write("┌─────────────────────────────────────────────────────────────────────\n")
    f.write("| Game Data for game " + str(game) + " of " +
            str(maxGames) + " | Rock Paper Scisors\n")
    f.write("| \n")
    f.write("| " + str(gameData) + "\n")
    f.write("| \n")
    f.write("└─────────────────────────────────────────────────────────────────────\n")
    f.write(" \n")
    f.close


def clear():
    system('clear')


game = 1

clear()
maxGames = int(input("How many games would you like to play? "))

gamemode = input(
    "What gamemode do you want?\n1. Player vs Player\n2. Player vs AI\n")

f = open(logFullPath + "game.log", "a")
f.write("\nGame Selected: Rock, Paper, Scissors made by MrSpudz\n")
f.write("┌─────────────────────────────────────────────────────────────────────\n")
f.write("| Number of Games: " + str(maxGames) + "\n")
f.write("| Gamemode:" + gamemode +
        "      1 = Player v Player   2 = Player v AI\n")
f.write("└─────────────────────────────────────────────────────────────────────\n")
f.write(" \n")
f.close()

if gamemode == "2":
    while game <= maxGames:
        clear()
        userInputRaw = input("Rock, Paper, Scissors: ")

        # Makes sure user input will always equal either rock, paper or scissors
        userInputLower = userInputRaw.lower()

        aiGen = randint(0, 2)

        if aiGen == 1:
            aiPick = "rock"
        elif aiGen == 2:
            aiPick = "paper"
        else:
            aiPick = "scissors"

    # Checks User input and AI input. Gives result
        if aiPick == userInputLower:
            print("Draw")
            gameData = "User Input: " + \
                str(userInputLower) + " | AI input: " + str(aiPick) + " | Draw"
            logData()
        elif aiPick == "rock" and userInputLower == "paper":
            print("You win")
            gameData = "User Input: " + \
                str(userInputRaw) + " | AI input: " + \
                str(aiPick) + " | User win"
            logData()
        elif aiPick == "rock" and userInputLower == "scissors":
            print("AI wins")
            gameData = "User Input: " + \
                str(userInputRaw) + " | AI input: " + str(aiPick) + " | AI win"
            logData()
        elif aiPick == "paper" and userInputLower == "rock":
            print("AI wins")
            gameData = "User Input: " + \
                str(userInputRaw) + " | AI input: " + str(aiPick) + " | AI win"
            logData()
        elif aiPick == "paper" and userInputLower == "scissors":
            print("You win")
            gameData = "User Input: " + \
                str(userInputRaw) + " | AI input: " + \
                str(aiPick) + " | User win"
            logData()
        elif aiPick == "scissors" and userInputLower == "paper":
            print("AI wins")
            gameData = "User Input: " + \
                str(userInputRaw) + " | AI input: " + str(aiPick) + " | AI win"
            logData()
        elif aiPick == "scissors" and userInputLower == "rock":
            print("You win")
            gameData = "User Input: " + \
                str(userInputRaw) + " | AI input: " + \
                str(aiPick) + " | User win"
            logData()
        else:
            print("Huh... That wasn't expected.")
            gameData = "User Input: " + \
                str(userInputRaw) + " | AI input: " + \
                str(aiPick) + " | Unexpected input"
            logData()

        game = game + 1
        sleep(1)

    print("\nThanks for playing :)")

    exit = str(input("Back to main menu (Any Key)"))

else:
    while game <= maxGames:
        clear()
        userInputRaw1 = input("Player 1: Rock, Paper, Scissors: ")

        # Makes sure user input will always equal either rock, paper or scissors
        userInputLower1 = userInputRaw1.lower()

        clear()
        userInputRaw2 = input("Player 2: Rock, Paper, Scissors: ")

        # Makes sure user input will always equal either rock, paper or scissors
        userInputLower2 = userInputRaw2.lower()

        if userInputLower1 == userInputLower2:
            print("Draw")
            gameData = "User Input: " + \
                str(userInputRaw1) + " | AI input: " + \
                str(userInputRaw2) + " | Draw"
            logData()
        elif userInputLower1 == "rock" and userInputLower2 == "paper":
            print("Player 2 Wins")
            gameData = "Player 1 Input: " + \
                str(userInputRaw1) + " | Player 2 input: " + \
                str(userInputRaw2) + " | Player 2 win"
            logData()
        elif userInputLower1 == "rock" and userInputLower2 == "scissors":
            print("Player 1 Wins")
            gameData = "Player 1 Input: " + \
                str(userInputRaw1) + " | Player 2 input: " + \
                str(userInputRaw2) + " | Player 1 Win"
            logData()
        elif userInputLower1 == "paper" and userInputLower2 == "rock":
            print("Player 1 Wins")
            gameData = "Player 1 Input: " + \
                str(userInputRaw1) + " | Player 2 input: " + \
                str(userInputRaw2) + " | AI win"
            logData()
        elif userInputLower1 == "paper" and userInputLower2 == "scissors":
            print("Player 2 Wins")
            gameData = "Player 1 Input: " + \
                str(userInputRaw1) + " | Player 2 input: " + \
                str(userInputRaw2) + " | User win"
            logData()
        elif userInputLower1 == "scissors" and userInputLower2 == "paper":
            print("Player 1 Wins")
            gameData = "Player 1 Input: " + \
                str(userInputRaw1) + " | Player 2 input: " + \
                str(userInputRaw2) + " | AI win"
            logData()
        elif userInputLower1 == "scissors" and userInputLower2 == "rock":
            print("Player 2 Wins")
            gameData = "Player 1 Input: " + \
                str(userInputRaw1) + " | Player 2 input: " + \
                str(userInputRaw2) + " | User win"
            logData()
        else:
            print("Huh... That wasn't expected.")
            gameData = "Player 1 Input: " + \
                str(userInputRaw1) + " | Player 2 input: " + \
                str(userInputRaw2) + " | Unexpected input"
            logData()

        game = game + 1
        sleep(1)

    print("\nThanks for playing :)")

    exit = str(input("Back to main menu (Any Key)"))


f = open(logFullPath + "game.log", "a")
f.write("Back to Menu\n")
f.close()
print("Exiting to main menu...")
sleep(1)
menu()
