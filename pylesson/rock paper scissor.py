import random

running = True

while running:
    choice = ['rock', 'paper', 'scissor']  # list of choice

    computer = random.choice(choice)
    player = input("rock, paper, scissor : ").lower()

    if player == computer:
        print("computer: "+computer)
        print("player: "+player)
        print("Tie!")

    if player == 'rock':
        if computer == 'scissor':
            print("computer: " + computer)
            print("player: " + player)
            print("Player Win")
        if computer == 'paper':
            print("computer: " + computer)
            print("player: " + player)
            print("Computer Win")

    if player == 'paper':
        if computer == 'rock':
            print("computer: " + computer)
            print("player: " + player)
            print("Player Win")
        if computer == 'scissor':
            print("computer: " + computer)
            print("player: " + player)
            print("Computer Win")

    if player == 'scissor':
        if computer == 'paper':
            print("computer: " + computer)
            print("player: " + player)
            print("Player Win")
        if computer == 'rock':
            print("computer: " + computer)
            print("player: " + player)
            print("Computer Win")

    exited = input("you want to play again (y/n)").lower()

    if exited != 'y':
        break