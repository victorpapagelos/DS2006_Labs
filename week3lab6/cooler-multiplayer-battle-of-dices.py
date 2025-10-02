#Dice functions
import random
def rollD6():
    """
    Roll a standard 6-sided dice.
    
    Returns:

        int: a random number between 1 and 6"""
    return random.randint(1, 6)

def rolld4():
    """
    Roll a standard 4-sided dice.
    
    Returns:

        int: a random number between 1 and 4"""
    return random.randint(1, 4)
def rolld8():
    """
    Roll a standard 8-sided dice.
    
    Returns:

        int: a random number between 1 and 8"""
    return random.randint(1, 8)
def rolld10():
    """
    Roll a standard 10-sided dice.
    
    Returns:

        int: a random number between 1 and 10"""
    return random.randint(1, 10)
def rolld12():
    """
    Roll a standard 12-sided dice.
    
    Returns:

        int: a random number between 1 and 12"""
    return random.randint(1, 12)
def rolld20():
    """
    Roll a standard 20-sided dice.
    
    Returns:

        int: a random number between 1 and 20"""
    return random.randint(1, 20)
def rolld100():
    """
    Roll a standard 100-sided dice.
    
    Returns:

        int: a random number between 1 and 100"""
    return random.randint(1, 100)  
    


player1_roll_dice = 0
player2_roll_dice = 0

print("Choose a dice to roll:")
print("1. D4")
print("2. D6")
print("3. D8")
print("4. D10")
print("5. D12")
print("6. D20")
print("7. D100")
choice = input("Enter your choice (Name of the dice): ")
print(choice)

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

    if choice=="D4":
        roll=rolld4
    elif choice=="D6":
        roll=rollD6
    elif choice=="D8":
        roll=rolld8
    elif choice=="D10":
        roll=rolld10
    elif choice=="D12":
        roll=rolld12
    elif choice=="D20":
        roll=rolld20
    elif choice=="D100":
        roll=rolld100
    else:
        choice == "Defaulted to D6"
        print("Invalid choice. Defaulting to D6.")
#Adds a round to the counter, starting from round 1
    rounds.append(1)
#Prints the lenght of the rounds list, in this case the latest and largest number of that list which is the current round
    print (f"\nRound {len(rounds)}")
    current_rolls=[]
#Rolls a dice depending on how many players are participating, and stores the values in a list
    for i in range (number_of_players):
        roll()
        current_rolls.append(roll())
        player_rolls_history[i].append(roll())
#Prints all the player rolls
        print(f"\nPlayer {player_names[i]} rolled: {roll()}")
        
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


