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
player1_roll1 = random.randint(1, 6)
player2_roll1 = random.randint(1, 6)
player1_roll2 = random.randint(1, 6)
player2_roll2 = random.randint(1, 6)
player1_roll3 = random.randint(1, 6)
player2_roll3 = random.randint(1, 6)
player1_roll4 = random.randint(1, 6)
player2_roll4 = random.randint(1, 6)
player1_roll5 = random.randint(1, 6)
player2_roll5 = random.randint(1, 6)
player1_roll6 = random.randint(1, 6)
player2_roll6 = random.randint(1, 6)
player1_roll7 = random.randint(1, 6)
player2_roll7 = random.randint(1, 6)
player1_roll8 = random.randint(1, 6)
player2_roll8 = random.randint(1, 6)

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll1 = random.randint(1, 6)
player2_roll1 = random.randint(1, 6)

print("Player 1 rolled: ", player1_roll1)
print("Player 2 rolled: ", player2_roll1)

if player1_roll1 > player2_roll1:
    print("Player 1 wins this round!")
    print("Because ", player1_roll1," is greater than ", player2_roll1)
    player1_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
elif player1_roll1 == player2_roll1:
    print("Amaaazzinng! This round has a tie!")
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll1," is greater than ", player1_roll1)
    player2_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 2
input("\nPress ENTER to roll the dice...")
player1_roll2 = random.randint(1, 6)
player2_roll2 = random.randint(1, 6)

print("Player 1 rolled: ", player1_roll2)
print("Player 2 rolled: ", player2_roll2)

if player1_roll2 > player2_roll2:
    print("Player 1 wins this round!")
    print("Because ", player1_roll2," is greater than ", player2_roll2)
    player1_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
elif player1_roll2 == player2_roll2:
    print("Amaaazzinng! This round has a tie!")
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll2," is greater than ", player1_roll2)
    player2_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 3
input("\nPress ENTER to roll the dice...")
player1_roll3 = random.randint(1, 6)
player2_roll3 = random.randint(1, 6)

print("Player 1 rolled: ", player1_roll3)
print("Player 2 rolled: ", player2_roll3)

if player1_roll3 > player2_roll3:
    print("Player 1 wins this round!")
    print("Because ", player1_roll3," is greater than ", player2_roll3)
    player1_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
elif player1_roll3 == player2_roll3:
    print("Amaaazzinng! This round has a tie!")
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll3," is greater than ", player1_roll3)
    player2_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
if player1_wins == 3:
    print("_________________________","\nRound |1| |2| |3|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|","\n_________________________")
elif player2_wins == 3:
    print("_________________________","\nRound |1| |2| |3|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|","\n_________________________")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

    # Round 4
player1_roll4 = random.randint(1, 6)
player2_roll4 = random.randint(1, 6)
input("\nPress ENTER to roll the dice...")
print("Player 1 rolled: ", player1_roll4)
print("Player 2 rolled: ", player2_roll4)

if player1_roll4 > player2_roll4:
    print("Player 1 wins this round!")
    print("Because ", player1_roll4," is greater than ", player2_roll4)
    player1_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
elif player1_roll4 == player2_roll4:
    print("Amaaazzinng! This round has a tie!")
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll4," is greater than ", player1_roll4)
    player2_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
if player1_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|","\n_________________________")
elif player2_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|","\n_________________________")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

player1_roll5 = random.randint(1, 6)
player2_roll5 = random.randint(1, 6)

input("\nPress ENTER to roll the dice...")
print("Player 1 rolled: ", player1_roll5)
print("Player 2 rolled: ", player2_roll5)

if player1_roll5 > player2_roll5:
    print("Player 1 wins this round!")
    print("Because ", player1_roll5," is greater than ", player2_roll5)
    player1_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
elif player1_roll5 == player2_roll5:
    print("Amaaazzinng! This round has a tie!")
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll5," is greater than ", player1_roll5)
    player2_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
if player1_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4| |5|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|", player1_roll5,"|", "\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|", player2_roll5,"|","\n_________________________")
elif player2_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4| |5|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|", player1_roll5,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|", player2_roll5,"|","\n_________________________")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

    input("\nPress ENTER to roll the dice...")
player1_roll6 = random.randint(1, 6)
player2_roll6 = random.randint(1, 6)

print("Player 1 rolled: ", player1_roll6)
print("Player 2 rolled: ", player2_roll6)

if player1_roll6 > player2_roll6:
    print("Player 1 wins this round!")
    print("Because ", player1_roll6," is greater than ", player2_roll6)
    player1_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
elif player1_roll6 == player2_roll6:
    print("Amaaazzinng! This round has a tie!")
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll6," is greater than ", player1_roll6)
    player2_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
if player1_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4| |5| |6|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|", player1_roll5,"|", player1_roll6,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|", player2_roll5,"|", player2_roll6,"|","\n_________________________")
elif player2_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4| |5| |6|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|", player1_roll5,"|", player1_roll6,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|", player2_roll5,"|", player2_roll6,"|","\n_________________________")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

    input("\nPress ENTER to roll the dice...")
player1_roll7 = random.randint(1, 6)
player2_roll7 = random.randint(1, 6)

print("Player 1 rolled: ", player1_roll7)
print("Player 2 rolled: ", player2_roll7)

if player1_roll7 > player2_roll7:
    print("Player 1 wins this round!")
    print("Because ", player1_roll7," is greater than ", player2_roll7)
    player1_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
elif player1_roll7 == player2_roll7:
    print("Amaaazzinng! This round has a tie!")
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll7," is greater than ", player1_roll7)
    player2_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
if player1_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4| |5| |6| |7|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|", player1_roll5,"|", player1_roll6,"|", player1_roll7,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|", player2_roll5,"|", player2_roll6,"|", player2_roll7,"|","\n_________________________")
elif player2_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4| |5| |6| |7|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|", player1_roll5,"|", player1_roll6,"|", player1_roll7,"|","\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|", player2_roll5,"|", player2_roll6,"|", player2_roll7,"|","\n_________________________")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
    

    input("\nPress ENTER to roll the dice...")
player1_roll8 = random.randint(1, 6)
player2_roll8 = random.randint(1, 6)

print("Player 1 rolled: ", player1_roll8)
print("Player 2 rolled: ", player2_roll8)

if player1_roll8 > player2_roll8:
    print("Player 1 wins this round!")
    print("Because ", player1_roll8," is greater than ", player2_roll8)
    player1_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
elif player1_roll8 == player2_roll8:
    print("Amaaazzinng! This round has a tie!")
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
else:
    print("Player 2 wins this round!")
    print("Because ", player2_roll8," is greater than ", player1_roll8)
    player2_wins += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
if player1_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4| |5| |6| |7| |8|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|", player1_roll5,"|", player1_roll6,"|", player1_roll7,"|", player1_roll8,"|", "\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|", player2_roll5,"|", player2_roll6,"|", player2_roll7,"|", player2_roll8,"|", "\n_________________________")
elif player2_wins == 3:
    print("_________________________","\nRound |1| |2| |3| |4| |5| |6| |7| |8|\n_________________________",)
    print("Player1|",player1_roll1,"|", player1_roll2,"|", player1_roll3,"|", player1_roll4,"|", player1_roll5,"|", player1_roll6,"|", player1_roll7,"|", player1_roll8,"|", "\n_________________________")
    print("Player2|",player2_roll1,"|", player2_roll2,"|", player2_roll3,"|", player2_roll4,"|", player2_roll5,"|", player2_roll6,"|", player2_roll7,"|", player2_roll8,"|", "\n_________________________")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")