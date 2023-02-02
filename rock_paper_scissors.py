import random

# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

options = ['scissors','rock','paper']
player_points = 0
computer_points = 0
ties = 0

play =True
rules = '''Rock beats Scissors
Scissors beats Paper
Paper beats Rock
'''
print("Welcome to Rock Scissors and Paper")
print("Here are the rules:")             
print(rules)

while play:
    player_input = input("Select (rock, scissors, paper or exit): \n").lower()
    if player_input == "exit":
        print(f"Player's total points: {player_points}\n")
        print(f"Computer's total points: {computer_points}\n")
        print(f"Total Number of ties: {ties}\n")
        break
    if player_input not in options:
        print("This is not valid please choose Rock, Paper or Scissors\n")
        
    else:
        computer_input = random.choice(options)
        if player_input =='rock' and computer_input=='scissors':
            print("Player chose rock and computer chose scissors\n")
            print("Rock beats scissors, Player Wins!\n")
            player_points+=1
        elif player_input =='scissors' and computer_input=='paper':
            print("Player chose scissors and computer chose paper\n")
            print("Scissors cuts paper, Player Wins!\n")
            player_points+=1
        elif player_input =='paper' and computer_input=='rock':
            print("Player chose paper and computer chose rock\n")
            print("Paper cover Rock, Player Wins!\n")
            player_points+=1

        elif player_input == computer_input:
            print(f"Player chose {player_input} and computer chose {computer_input}\n")
            print("it's a tie!\n")
            ties+= 1
        
        else:
            print(f"Player chose {player_input} and computer chose {computer_input}\n")
            print(f"{computer_input} beats {player_input}, Computer Wins!\n")
            computer_points+=1



    