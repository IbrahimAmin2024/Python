# rock, paper, scissors

import random

while True: #false
    choices = ["rock", "paper","scissors"] #set [] Dictionary/
    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? : ").lower()

        if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print("Tie!, equals, Restarting...")

        elif ( player == "rock"):
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("lose.")

            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("win.")

        elif ( player == "scissors"):
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("lose.")

            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("win.")

        elif (player == "paper"):
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("lose.")

            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("win.")

    play_again = input("Play again : ").lower()

    if play_again != "yes": #no
        break

print("Bye")
