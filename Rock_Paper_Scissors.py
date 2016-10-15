# Rock Paper Scissors yall!
from random import randint
from time import sleep

options = ["R", "P","S"]
LOST = "You lost! Please try again!"
WON = "Yay! You won!"

def decide_winner(user_choice, computer_choice):
    print "You selected: %s" % user_choice
    print "Computer selecting..."
    sleep(1)
    print "You selected: %s" % computer_choice
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print "It's a tie!"
    elif user_choice_index == 0 and computer_choice_index == 2:
        print WON
    elif user_choice_index == 1 and computer_choice_index == 0:
        print WON
    elif user_choice_index == 2 and computer_choice_index == 1:
        print WON
    elif user_choice_index > 2:
        print "Invalid Option!"
        return
    else:
        print LOST

def play_RPS():
    print "Rock, Paper, or Scissors?"
    user_choice = raw_input("Select R for Rock, P for Paper or S for Scissors: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,len(options)-1)]
    decide_winner(user_choice, computer_choice)

play_RPS()
