import sys
import player
import dice

def main():
    
    number_of_players = input("Enter number of players (1/2): ")

    player1_score = 0
    player2_score = 0

    player_turn = 0

    p1 = player.Player()
    p1.setName(True)

    if number_of_players == "1":
        p2 = player.Player()
        p2.name = "Computer"

    if number_of_players == "2":
        p2 = player.Player()
        p2.setName(False)
    
    print(p1.name)
    print(p2.name)

    while player1_score < 100 and player2_score < 100:
        
        if player_turn == 0:
            die = dice.Dice()
            roll = die.roll_dice()
            print(roll)

            if roll != 1:
                hold = input("Do you want to hold (y/n): ")
                if hold == "y":
                    player1_score += roll
                    player_turn = 1
                    continue
                else:
                    print("continue")
        
        else:
            print("Player 2 turn")



main()
