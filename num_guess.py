#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 09 25, 2026
# This file where constants are stored for num_guess.py


import constants


def main():

    # Get a guessed number from the user
    guessed = int(input("Guess a random number in the range of 0-9: "))

    # check if the number is the same as the correct number

    if guessed == constants.CORRECT_NUMBER:

        # If correct then tell the user they guessed correctly
        print("You Guessed Correctly!")

    if guessed != constants.CORRECT_NUMBER:

        # If not correct then tell the user they guessed incorrectly
        print("You Guessed Incorrectly!")


if __name__ == "__main__":
    main()
