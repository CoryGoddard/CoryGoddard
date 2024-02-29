import random as rand
from colorama import Fore
from os import system, name

def main():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    greenChars = []
    yellowChars = []
    grayChars = []
    attempts = 0
    guesses = []

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # print welcome screen
    print(" __________________________________________________")
    print("|  __        __                     _   _          |\n" +
          "|  \ \      / /   ___    _ __    __| | | |   ___   |\n" +
          "|   \ \ /\ / /   / _ \  | '__|  / _` | | |  / _ \  |\n" +
          "|    \ V  V /   | (_) | | |    | (_| | | | |  __/  |\n" +
          "|     \_/\_/     \___/  |_|     \__,_| |_|  \___|  |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|" + "WORDLE Clone".center(len("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")) + "|\n" +
          "|" + "Created By: Cory Goddard".center(len("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")) + "|\n" +
          "|" + "Last Modified: Sep.28th 2023".center(len("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")) + "|")
    print("|__________________________________________________|")

                                               

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # decide difficulty
    wordLength = input("\nHow many characters for the word(4-9)? ")

    while not wordLength.isdigit() or int(wordLength) < 4 or int(wordLength) > 9:
        wordLength = input("\nInvalid Input.\nHow many characters for the word(4-9)? ")
    
    wordLength = int(wordLength)

    display = "~" * wordLength

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # determine the goal word
    goalWord = getWord(wordLength)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # begin loop until word guessed or attempts = 6
    done = False
    while not done:
        
        displayAll(letters, greenChars, yellowChars, grayChars, attempts, display, guesses)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        attempts += 1

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # get a guess

        guess = input("Enter guess: ")
        
        while len(guess) != wordLength or not isGuessLegal(guess):
            guess = input("Guess not valid.\nEnter guess: ")

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # score their guess
        score, greenChars, yellowChars, grayChars = scoreGuess(guess, goalWord, greenChars, yellowChars, grayChars)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # if guess is correct, print attempts taken and good job message
        # else print thier "score", or the green/yellow/gray characters
        # and loop again if attempts < 6
        # if attempts == 6 and guess not correct, display goal and 
        # better luck next time message
        if guess.lower() == goalWord.lower():
            guesses.append(score)
            displayAll(letters, greenChars, yellowChars, grayChars, attempts, display, guesses)
            
            print(" ___________________________________________________________________\n"
                  "|   ____                         _           _           _       _  |\n" +
                  "|  / ___|  _ __    ___    __ _  | |_        | |   ___   | |__   | | |\n" +
                  "| | |  _  | '__|  / _ \  / _` | | __|    _  | |  / _ \  | '_ \  | | |\n" +
                  "| | |_| | | |    |  __/ | (_| | | |_    | |_| | | (_) | | |_) | |_| |\n" +
                  "|  \____| |_|     \___|  \__,_|  \__|    \___/   \___/  |_.__/  (_) |\n" +
                  "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            
            print("|" + f"You got the word in {attempts} attempts!".center(len("___________________________________________________________________")) + "|")
            print("|___________________________________________________________________|")
            done = True
        else:
            if attempts == 6:
                guesses.append(score)
                displayAll(letters, greenChars, yellowChars, grayChars, attempts, display, guesses)
                print("Better luck next time!\nThe word was: " + goalWord)
                done = True
            else:
                done = False
                guesses.append(score)
                #displayAll(letters, greenChars, yellowChars, grayChars, attempts, display, guesses)

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def displayAll(letters, greenChars, yellowChars, grayChars, attempts, display, guesses):
    clear()

    fullString = ""

    if len(display) % 2 == 0:
        margin = (14 - len(display)) // 2
        even = True
    else:
        margin = (13 - len(display)) // 2
        even = False
    
    for guess in guesses:
        fullString += " " * margin + (guess + "\n")

    for i in range(0,6-attempts):
        fullString += " " * margin + (display + "\n")

    result = ""

    for letter in letters:
        if letter in greenChars:
            result += (Fore.GREEN + letter + Fore.RESET)
        elif letter in yellowChars:
            result += (Fore.YELLOW + letter + Fore.RESET)
        elif letter in grayChars:
            result += (Fore.BLACK + letter + Fore.RESET)
        else:
            result += (Fore.WHITE + letter + Fore.RESET)

    if even:
        fullString += "~~~~~~~~~~~~~~\n"
        fullString += "|  " + result[:result.index("h")+1] + Fore.RESET + "  |\n"
        fullString += "|  " + result[result.index("h")+1:result.index("p")+1] + Fore.RESET + "  |\n"
        fullString += "|  " + result[result.index("p")+1:result.index("x")+1] + Fore.RESET + "  |\n"
        fullString += "|     " + result[result.index("x")+1:] + Fore.RESET + "     |\n"
        fullString += "~~~~~~~~~~~~~~\n"
    else:
        fullString += "~~~~~~~~~~~~~\n"
        fullString += "|  " + result[:result.index("g")+1] + Fore.RESET + "  |\n"
        fullString += "|  " + result[result.index("g")+1:result.index("n")+1] + Fore.RESET + "  |\n"
        fullString += "|  " + result[result.index("n")+1:result.index("u")+1] + Fore.RESET + "  |\n"
        fullString += "|   " + result[result.index("u")+1:] + Fore.RESET + "   |\n"
        fullString += "~~~~~~~~~~~~~\n"

    print(fullString)

def scoreGuess(guess, goal, greenChars, yellowChars, grayChars):
    guess = guess.lower()
    goal = goal.lower()

    result = ""
    listed = []

    for i in range(0, len(guess)):
        if guess[i] == goal[i]:
            listed.append(f"{Fore.GREEN}{guess[i]}")
            number = goal.count(guess[i])
            if greenChars.count(guess[i]) < number:
                greenChars.append(guess[i])

        elif guess[i] in goal:
            yellowChars.append(guess[i])
            numGoal = goal.count(guess[i])
            numGuess = guess.count(guess[i])
            
            if numGuess > numGoal:
                temp = [x for x in guess]
                indexes = []
                for amount in range(numGoal):
                    indexes.append(temp.index(guess[i]))
                    temp[temp.index(guess[i])] = " "

                if not i in indexes:
                    listed.append(f"{Fore.BLACK}{guess[i]}")
                else:
                    if goal.count(guess[i]) >= guess.count(guess[i]):
                        listed.append(f"{Fore.YELLOW}{guess[i]}")
                    else:
                        listed.append(f"{Fore.BLACK}{guess[i]}")
            else:
                listed.append(f"{Fore.YELLOW}{guess[i]}")

        else:
            grayChars.append(guess[i])
            listed.append(f"{Fore.BLACK}{guess[i]}")

    for i in listed:
        result += i

    return (result + Fore.RESET), greenChars, yellowChars, grayChars
        
def isGuessLegal(guess):
    file = open("words.txt", "r")
    contents = file.readlines()
    file.close()

    if (guess.lower() + "\n") in contents:
        return True
    else:
        return False

def getWord(length):
    possibleWords = []
    file = open("words.txt", "r")

    contents = file.readlines()

    file.close()

    for line in contents:
        word = line.rstrip()
        if len(word) != length:
            continue
        else:
            possibleWords.append(word)

    wordIndex = rand.randint(0, len(possibleWords) - 1)

    chosen = possibleWords[wordIndex]

    return chosen

main()