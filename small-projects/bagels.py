import random
from types import coroutine

MAX_DIGITS = 3
GUESSES = 3

#Generate secret number, define guess counter and the correct guess boolean flag.
secretNumber = random.randint(1, 999)
secretNumberString = str(secretNumber)
guessCounter = 10
correctGuess = False

print("Welcome to Bagels!")
print("You will have 10 guesses to figure out what the secret number is.")
print("When I saw \"Pico\", one digit is correct but in the wrong position.")
print("When I say \"Fermi\", one digit is correct and in the right position.")
print("When I say \"Bagels\", no digit is correct.")
print("----------------------------\n")
print("Debug: The secret number is " + secretNumberString)

while correctGuess is False and guessCounter > 0:
    print("Guesses remaining: " + str(guessCounter))
    userGuess = input("Input your guess: ")
    numUserGuess = 0
    if userGuess.isdigit():
        numUserGuess = int(userGuess)

    if numUserGuess <= 999 and numUserGuess > 1:
        if userGuess == secretNumberString:
            correctGuess = True
        elif userGuess[0:1] is secretNumberString[0:1] or userGuess[1:2] is secretNumberString[1:2] or userGuess[2:3] is secretNumberString[2:3]:
            print("Pico!")
        elif userGuess[0:1] is secretNumberString[1:2] or userGuess[0:1] is secretNumberString[2:3] or userGuess[1:2] is secretNumberString[0:1] or userGuess[1:2] is secretNumberString[2:3]or userGuess[2:3] is secretNumberString[0:1] or userGuess[2:3] is secretNumberString[1:2]:
            print("Fermi!")
        else:
            print("Bagels!")

        guessCounter -= 1
    else:
        print("Invalid input. Please enter a valid 3 digit number. Include leading 0's as needed.")

if correctGuess is True:
    print("Congratulations! You guess it right. The secret number was " + secretNumberString)
else:
    print("Bummer, you didn't get it right. The secret number was " + secretNumberString)
