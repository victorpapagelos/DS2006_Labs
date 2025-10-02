import random

    # Variables to keep track of the score
player1_wins=0
player2_wins=0
gameover=False
rounds=0

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


#A list that stores the rolls of each player

list_of_player1_rolls = []
list_of_player2_rolls = []

#A list that stores the rounds played

round_list = []

#a while loop that continues until one player wins 3 times

while not gameover:

#Adds 1 to the round counter each time the loop runs

    rounds +=1

#Prints the round number 

    print("\nRound", rounds)

#Rolls the desired dice based on user input

    if choice == "D4":
        player1_roll_dice = rolld4()
        player2_roll_dice = rolld4()
    elif choice == "D6":
        player1_roll_dice = rollD6()
        player2_roll_dice = rollD6()
    elif choice == "D8":
        player1_roll_dice = rolld8()
        player2_roll_dice = rolld8()
    elif choice == "D10":
        player1_roll_dice = rolld10()
        player2_roll_dice = rolld10()
    elif choice == "D12":
        player1_roll_dice = rolld12()
        player2_roll_dice = rolld12()
    elif choice == "D20":
        player1_roll_dice = rolld20()
        player2_roll_dice = rolld20()
    elif choice == "D100":
        player1_roll_dice = rolld100()
        player2_roll_dice = rolld100()
    else:

#If the user input is invalid, the program defaults to D6 and prints Invalid

        choice == "Defaulted to D6"
        print("Invalid choice. Defaulting to D6.")

    #Assigns D6 rolls to both players

        player1_roll_dice=rollD6()
        player2_roll_dice=rollD6()
        
#Prompts the user to press ENTER in order to roll the dice for player 1

    input("\nPress ENTER to roll the dice for Player 1\n")

#Prints the result of player 1's roll and appends it to the list of rolls as well as the round number to the round list

    print("\nPlayer 1 rolled:", player1_roll_dice)
    list_of_player1_rolls.append(player1_roll_dice)
    round_list.append(rounds)

#Prompts the user to again press ENTER in order to roll the dice for player 2

    input("\nPress ENTER to roll the dice for Player 2\n")

#Prints the result of player 2's roll and appends it to the list of rolls

    print("Player 2 rolled:", player2_roll_dice)
    list_of_player2_rolls.append(player2_roll_dice)

#Compares the two rolls and gives a point/win to the player with the higher roll, printing the current score

    if  player1_roll_dice > player2_roll_dice:
        player1_wins += 1
        print("\nCurrent score:\nPlayer 1:", player1_wins, "\nPlayer 2:", player2_wins)
    elif player2_roll_dice > player1_roll_dice:
        player2_wins += 1
        print("\nCurrent score:\nPlayer 1:", player1_wins, "\nPlayer 2:", player2_wins)

#If the rolls are equal, prints that the round is a tie and no points are awarded

    elif player1_roll_dice==player2_roll_dice:
        print("This round is a tie! No points awarded.")

#Checks if either player meets the requirement of 3 wins to end the game and declare a winner, printing a table of results.

    if player1_wins == 3: 
            gameover = True, print("Player 1 wins!")
            print("\nType of dice:", player1_roll_dice,)
            print("| Rounds played ",rounds)
            print("| Round Counter |",round_list, "|")
            print("| Player 1 rolls |",list_of_player1_rolls, "|")
            print("| PLayer 2 rolls |",list_of_player2_rolls, "|")
    elif player2_wins == 3:
        gameover = True, print("Player 2 wins!")
        print("\nType of dice:", choice)
        print("| Rounds played |", rounds)
        print("| Round Counter |",round_list, "|")
        print("| Player 1 rolls |",list_of_player1_rolls, "|")
        print("| Player 2 rolls |",list_of_player2_rolls, "|")
        
filename=input("Enter the filename to save the results: ")
with open(filename, 'w') as file: 

# 'w' = write mode

    for i in range(len(list_of_player1_rolls)):
        file.write(f"Round, {round_list[i]}, Player 1 roll, {list_of_player1_rolls[i]}, Player 2 roll, {list_of_player2_rolls[i]}\n")