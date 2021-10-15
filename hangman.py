from random import randint

import random

def displayIntro():
    print("_______________________________________________\n"
          "_\n"
          "||\n"
          "||__ ______ _________ ______\n"
          "| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n"
          "| | | | (_| | | | | (_| | | | | | | (_| | | | |\n"
          "|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n"
          "                    __/ |\n"
          "                   |___/\n"
          "_______________________________________________\n"
          "_____________________Rules_____________________\n"
          "Try to guess the hidden word one letter at a\n"
          "time. The number of dashes are equivalent to\n"
          "the number of letters in the word. If a player\n"
          "suggests a letter that occurs in the word,\n"
          "blank places containing this character will be\n"
          "filled with that letter. If the word does not\n"
          "contain the suggested letter, one new element\n"
          "of a hangman’s gallow is painted. As the game\n"
          "progresses, a segment of a victim is added for\n"
          "every suggested letter not in the word. Goal is\n"
          "to guess the word before the man hangs!\n"
          "\n"
          "Good Luck!!!")


def displayEnd(result):
    if not result:
        # print("\nCongratulations! You guessed the word correctly and won the game! \n")
        print(" __     __           _           _   _\n"
              " \ \   / /          | |         | | | |\n"
              "  \ \_/ /__  _   _  | | ___  ___| |_| |\n"
              "   \   / _ \| | | | | |/ _ \/ __| __| |\n"
              "    | | (_) | |_| | | | (_) \__ \ |_|_|\n"
              "    |_|\___/ \__,_| |_|\___/|___/\__(_)\n"
              "_______ _                                        _ _          _ _ \n"
              "       |__   __| |                                      | (_)        | | |\n"
              "          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |\n"
              "          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |\n"
              "          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|\n"
              "          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)\n"
              "__________________________________________________________________________\n")
    else:
        print("          _                                  _\n"
              "         (_)                                (_)\n"
              "__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    \n"
              "\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|\n"
              " \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ | \n"
              "  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|  \n"
              "           | |   (_)    | |                  | (_)\n"
              "        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ \n"
              "       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|\n"
              "      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ | \n"
              "       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_| \n"
              "________________________________________________________________________\n")


def displayHangman(state):
    if state == 5:
        print("    ._______.\n"
              "    |\n"
              "    |\n"
              "    |\n"
              "    |\n"
              "    |\n"
              "    |\n"
              "____|___")
    if state == 4:
        print("    ._______.\n"
              "    |/      |\n"
              "    |      (_)\n"
              "    |\n"
              "    |\n"
              "    |\n"
              "    |\n"
              "____|___")
    if state == 3:
        print("    ._______.\n"
              "    |/      |\n"
              "    |      (_)\n"
              "    |       |\n"
              "    |\n"
              "    |\n"
              "    |\n"
              "____|___")
    if state == 2:
        print("    ._______.\n"
              "    |/      |\n"
              "    |      (_)\n"
              "    |      \|/\n"
              "    |\n"
              "    |\n"
              "    |\n"
              "____|___")
    if state == 1:
        print("    ._______.\n"
              "    |/      |\n"
              "    |      (_)\n"
              "    |      \|/\n"
              "    |       |\n"
              "    |       |\n"
              "    |\n"
              "____|___")
    if state == 0:
        print("    ._______.\n"
              "    |/      |\n"
              "    |      (_)\n"
              "    |      \|/\n"
              "    |       |\n"
              "    |       |\n"
              "    |      / \ \n"
              "____|___")

def getWord():
    file1 = open('hangman-words.txt', 'r')
    Lines = file1.readlines()
    word = Lines[random.randint(0, len(Lines)-1)]
    return word

def valid(c):
    return len(c) == 1 and ord(c) >= 97 and ord(c) <= 122

def play():
    print("\n\n")
    word = getWord()
    lives = 5
    outword = ""
    guessedletters = []
    for x in range (len(word)-1):
        outword+="*"
    displayHangman(lives)
    print(outword)
    inpt = input()
    guessed = False
    while lives > 0 and not guessed:
        while not valid(inpt):
            print("\nPlease write one English lowercase letter.")
            inpt = input(outword + "\n")
        correct = False
        for x in range(len(word)-1):
            if word[x] == inpt:
                guessedletters.append(inpt)
                correct = True
                break
        if not correct:
            lives -= 1
        else:
            outword = ""
            for x in range(len(word)-1):
                if word[x] in guessedletters:
                    outword+=word[x]
                else:
                    outword+="*"
            if '*' not in outword:
                guessed = True
                print("\nThe hidden word was - "+word)
                break
        if lives == 0:
            print("\nThe hidden word was - " + word)
            break
        displayHangman(lives)
        print("\n")
        inpt = input(outword + "\n")

    if guessed:
        return True
    else:
        return False



def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        ans = input("Would you like to play one more game? (y/n)\n")
        if ans == "n" or ans == "N":
            print("\nIt was a pleasure to play with you! See you next time...")
            break
        print("\n\n")
        # TODO


if __name__ == "__main__":
    hangman()


