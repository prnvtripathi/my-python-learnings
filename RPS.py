import random


def getChoices():
    userChoice = input("Enter a choice (rock, paper, scissors): ")
    computerChoiceList = ['paper', 'rock', 'scissors']
    computerChoice = random.choice(computerChoiceList)

    choices = {'player': userChoice, 'computer': computerChoice}

    return choices


def checkWin(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == 'rock':
        if computer == 'scissors':
            print("You won!")
        elif computer == "paper":
            print("You lose.")
        else:
            print("It's a tie.")
    elif player == 'paper':
        if computer == 'rock':
            print("You won!")
        elif computer == "scissors":
            print("You lose.")
        else:
            print("It's a tie.")
    else:
        if computer == 'paper':
            print("You won!")
        elif computer == "rock":
            print("You lose.")
        else:
            print("It's a tie.")

choices = getChoices()
checkWin(choices['player'], choices['computer'])