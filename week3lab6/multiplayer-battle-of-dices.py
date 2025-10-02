#Dice function
import random

def rolld6():
    return random.randint(1, 6)

#Different variables
winning_score = 3
rounds=[]
player_names=[]
player_wins=[]
player_rolls_history = []
gameover=False
winners=[]

#Prompts the player to input how many players are going to play
number_of_players = int(input("How many players?"))

#Depending on the number of players, the user can write x amount of names and add it to an empty list
for i in range (number_of_players):
    name=input(f"\nWhat is the name of player {i+1}?")
    player_names.append(name)
    player_wins.append(0)
    player_rolls_history.append([])

#while loop that ends once a player reaches 3 wins
while gameover is False:

#Adds a round to the counter, starting from round 1
    rounds.append(1)
#Prints the lenght of the rounds list, in this case the latest and largest number of that list which is the current round
    print (f"\nRound {len(rounds)}")
    current_rolls=[]
#Rolls a dice depending on how many players are participating, and stores the values in a list
    for i in range (number_of_players):
        roll=rolld6()
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
#Prints all the player rolls
        print(f"\nPlayer {player_names[i]} rolled: {roll}")
        
#Grabs the highest numbers from the list
    max_roll=max(current_rolls)
#Resets the winners, else it would print the entire list in future rounds instead of the current round winner(s)
    winners=[]
    
#Adds a win to the player(s) with the highest rolls
    for j in range (len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j]+=1
#Prints the winning players(s) and what they rolled
    print(f"\nWinners of this round are: {', '.join(winners)}", f", They rolled a {max_roll}")
    
#Prints the current scores
    print("\nCurrent Scores:")
    for i in range (number_of_players):
        print(f"{player_names[i]}:, {player_wins[i]}")
#Prompts the user to continue the battle
    input("\nPress ENTER to continue")
#Gameover condition is if a player wins 3 times, then the game is ended and a message says so.
    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print(f"\n {player_names[z]} is the newset battle of dices champion")
            gameover = True


