# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 12)
player2_roll = random.randint(1, 12)

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

if player1_roll > player2_roll:
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the best dice player ever seen, edging their opponent out to win the game!")
elif player2_wins == 3:
    print("Player 2 is the best dice player ever seen, edging their opponent out to win the game!")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.

input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 12)
player2_roll = random.randint(1, 12)

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

if player1_roll > player2_roll:
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the best dice player ever seen, edging their opponent out to win the game!")
elif player2_wins == 3:
    print("Player 2 is the best dice player ever seen, edging their opponent out to win the game!")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.
