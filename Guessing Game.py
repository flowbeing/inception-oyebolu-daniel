# Guessing Game

secretWord = "SecretWord"

Guess = ""

guessnumber = 1

while (Guess != secretWord) and guessnumber < 4:
    Guess = input("Enter your pass: ")
    if Guess != secretWord:
        print("You entered the wrong Password")
        guessnumber += 1
    elif Guess == secretWord:
        print("You will be redirected shortly")

    if guessnumber == 4:
        print("You've exceeded the maximum number of tries.")
