from random import randint
from os import path,system
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
            str(maxGames) + " | Guess the Number\n")
    f.write("| \n")
    f.write("| " + str(gameData) + "\n")
    f.write("└─────────────────────────────────────────────────────────────────────\n")
    f.write(" \n")
    f.close


def clear():
    system('clear')


round = 1
randomNum = 0
attempt = 0
game = 1

f = open(logFullPath + "game.log", "a")
f.write("\nGame Selected: Guess The Number made by MrSpudz\n")
f.write("┌─────────────────────────────────────────────────────────────────────\n")
f.write("| Game Settings\n")
f.write("| Difficulty settings : 1 = Easy, 2 = Medium, 3 = Hard")
f.write(" \n")
f.close()


# Menu
clear()
print("Difficulty Selection:")
print("Please select a difficulty.")
print("1: Easy (1-20)")
print("2: Medium (1-50)")
print("3: Hard (1-100)")

difficulty = input("Select Difficulty: ")

f = open(logFullPath + "game.log", "a")
f.write("| Selected difficulty: " + str(difficulty) + "\n")
f.close()


# Difficulty Detection
if difficulty == "1":
    mode = "easy"
    clear()
elif difficulty == "2":
    mode = "medium"
    clear()
elif difficulty == "3":
    mode = "hard"
    clear()
else:
    print("Error. Closing Program.")
    sleep(1)
    f = open(logFullPath + "game.log", "a")
    f.write("Program crashed. Exit code (1)")
    f.close()
    quit()

maxGames = int(input("How many games would you like to play? "))

f = open(logFullPath + "game.log", "a")
f.write("| Number of Games: " + str(maxGames) + "\n")
f.write("└─────────────────────────────────────────────────────────────────────\n")
f.write(" \n")
f.close()

# Game Loop

while game <= maxGames:
    clear()
    guess = ""
    attempt = 0
    score = 10

    if mode == "easy":
        randomNum = randint(1, 20)
    elif mode == "medium":
        randomNum = randint(1, 50)
    elif mode == "hard":
        randomNum = randint(1, 100)
    else:
        print("An unexpected error occurred. Closing Program")
        quit()

    while guess != randomNum:
        print("Game " + str(game) + " of " + str(maxGames))
        guess = int(input("Guess a number: "))

        if guess == randomNum:
            attempt = attempt + 1
            print("Well done! You guessed the number")
            print("Your score was: " + str(score))
            print("You had " + str(attempt) + " attempts")

            gameData = "Attempts: " + \
                str(attempt) + "    Score: " + str(score) + "/10"

            logData()

            game = game + 1
            sleep(1)
            break

        if guess > randomNum:
            print("Sorry but that isn't the right number. Try going lower.")
            score = score - 1
            attempt = attempt + 1
            sleep(1)
            clear()

        if guess < randomNum:
            print("Sorry but that isn't the right number. Try going higher.")
            score = score - 1
            attempt = attempt + 1
            sleep(1)
            clear()

print("\nThanks for playing :)")

exit = str(input("Back to main menu (Any Key)"))

f = open(logFullPath + "game.log", "a")
f.write("Back to Menu\n")
f.close()
print("Exiting to main menu...")
sleep(1)
menu()
