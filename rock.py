#Rock Paper Scissors

import random

choices = ["rock", "paper", "scissors"]

human = raw_input("Rock, Paper, Scissors!: ")
computer = random.choice(choices)

if human == computer:
    game(human)

if (human != "rock" and human != "paper" and human != "scissors"):
    print "Computor: scissors"
    print "Try again!"

if human == "rock" and computer == "paper":
    print "Computor: paper"
    print "You lose!"

if human == "rock" and computer == "scissors":
    print "Computor: scissors"
    print "You win!"

if human == "scissors" and computer == "paper":
    print "Computor: paper"
    print "You win!"

if human == "scissors" and computer == "rock":
    print "Computor: rock"
    print "You lose!"

if human == "paper" and computer == "rock":
    print "Computor: rock"
    print "You win!"

if human == "paper" and computer == "scissors":
    print "Computor: scissors"
    print "You lose!"
