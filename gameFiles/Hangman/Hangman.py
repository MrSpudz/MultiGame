from random import random
from os import path,system
from time import sleep

# Log Relative Path Setup
absolutePath = path.dirname(__file__)
logRelPath = "../logs"
logFullPath = path.join(absolutePath, logRelPath)

# Main Relative Path Setup
absolutePath = path.dirname(__file__)
relPath = "../main/"
fullPath = path.join(absolutePath, relPath)

attempt = 0
game = 1

def main():
    chosenWord = pick_word()
    game(chosenWord)
    while game != maxGames:
        chosenWord = pick_word(chosenWord)
        game(chosenWord)

def pick_word():
    lines = open(absolutePath + '/Hangman/words_alpha.txt').read().splitlines()
    chosenWord = str(random.choice(lines))
    return chosenWord

def game(chosenWord):
    wordCompletion = "_ " * len(chosenWord)
    guessed = False
    tries = 6
    guessedLetters = []
    guessedWords = []
    print(wordCompletion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed this letter!"),
            elif guess not in chosenWord:
                print(guess, " is not in the word."),
                guessedLetters.append(guess),
                tries = tries - 1
            else:
                print("Good job, ", guess, " is in the word!")
                guessedLetters.append(guess)
                wordAsList = list(wordCompletion)
                indices = [pos for pos, letter in enumerate(chosenWord) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = "".join(wordAsList)
                if "_" not in wordCompletion:
                    guessed = True

        elif len(guess) == len(chosenWord) and guess.isalpha():

            if guess in guessedWords:
                print("You already guessed this word!"),
            elif guess != chosenWord:
                print(guess, " is not the word."),
                guessedWords.append(guess)
                tries = tries - 1
            else:
                guessed = True
                wordCompletion = chosenWord

        else:
            print("Invalid Guess")
            print(wordCompletion)

    if guessed:
        print("Congrats! You guessed the word!")

def menu():
    with open(fullPath + "start.py") as f:
        exec(f.read())


def logData():
    f = open(logFullPath + "game.log", "a")
    f.write("┌─────────────────────────────────────────────────────────────────────\n")
    f.write("| Game Data for game " + str(game) + " of " +
            str(maxGames) + " | Guess the Number\n")
    f.write("| \n")
    #f.write("| " + str(gameData) + "\n")
    f.write("└─────────────────────────────────────────────────────────────────────\n")
    f.write("\n")
    f.close


def clear():
    system('clear')

maxGames = int(input("How many games would you like to play? "))

f = open(logFullPath + "game.log", "a")
f.write("\nGame Selected: Hangman made by MrSpudz\n")
f.write("┌─────────────────────────────────────────────────────────────────────\n")
f.write("| Game Settings\n")
f.write("| Number of Games: " + str(maxGames) + "\n")
f.write("└─────────────────────────────────────────────────────────────────────\n")
f.write(" \n")
f.close()

if __name__ == "__main__":
    main()