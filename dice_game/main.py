import sys
import player

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
        player1_score += 25
        
        if player_turn == 0:
            print()



main()
