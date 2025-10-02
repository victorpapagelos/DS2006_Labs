import random

    # Variables to keep track of the score
player1_wins=0
player2_wins=0
gameover=False
player1_points=0
player2_points=0

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
    
def choose_dice():
    """
    Choose a dice to roll.
    
    Returns:
        function: a function that rolls the chosen dice
    """
    print("Choose a dice to roll:")
    print("1. D4")
    print("2. D6")
    print("3. D8")
    print("4. D10")
    print("5. D12")
    print("6. D20")
    print("7. D100")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        return rolld4
    elif choice == "2":
        return rollD6
    elif choice == "3":
        return rolld8
    elif choice == "4":
        return rolld10
    elif choice == "5":
        return rolld12
    elif choice == "6":
        return rolld20
    elif choice == "7":
        return rolld100
    else:
        print("Invalid choice. Defaulting to D6.")
        return rollD6
    
    
player1_roll_dice = choose_dice()
player2_roll_dice = choose_dice()

for round_num in range(2):
    input(f"\nRound {round_num + 1} Press ENTER to roll the dice")
    player1_roll = player1_roll_dice()
    player2_roll = player2_roll_dice()
    player1_points += player1_roll
    player2_points += player2_roll
    print("Current score:\nPlayer 1:", player1_points, "\nPlayer 2:", player2_points)

if player1_points > player2_points:
    print("Game Over! Player 1 wins!")
else:
    print("Game Over! Player 2 wins!")
