import random
from pyfiglet import figlet_format
from time import sleep
from termcolor import colored, cprint
import os
import sys
import time

def loading_animation():
    for _ in range(3):
        for _ in range(3):  # Adjust the range based on the number of dots you want
            sys.stdout.write("Number Loading" + "." * (_ % 3 + 1) + "\r")
            sys.stdout.flush()
            time.sleep(0.5)  # Adjust the sleep duration as needed
        sys.stdout.write(" " * 20 + "\r")
        sys.stdout.flush()
    cprint("\nThank you d(-_☆)\n", 'blue')


def titleSequence():
    cprint("*****************************************************************", 'blue')
    title = figlet_format("Number Guessing Game", font="speed", justify="center", width=70)
    cprint(title, 'blue')
    cprint("*****************************************************************", 'blue')
    cprint("\n------- This is a Number Guessing Game that uses Python  -------", 'blue')
    cprint("\nThe rules are simple, you will pick a range for the number and \nI will tell you based on your input if you are correct or not!", 'yellow')
    cprint("\n*** LETS BEGIN (⌐▨_▨) \n", 'blue')

def footSequence():
    foot = figlet_format("YOU WIN", justify="center", width=70)
    cprint(foot, 'blue')

def defineNumber():
    while True:
        try:
            guessRange = int(input("Please pick the range of the number: "))
            number = random.randrange(1, guessRange)
            break
        except ValueError:
            print("Sorry, that is not a valid number!\n")
    return number

def guessTheNumber(number):
    selection = 0
    while selection != number:
        while True:
            try:
                selection = int(input("\nWhat number am I thinking of: "))
                if selection < number:
                    print("\ntoo low")
                elif selection > number:
                    print("\ntoo high")
                break
            except ValueError:
                print("Sorry that is not a valid guess!\n")
    footSequence()


titleSequence()
rangeSelection = defineNumber()
loading_animation()
guessTheNumber(rangeSelection)













