import player
import dice
import intelligence

def main():

    print("\nWELCOME TO PIG (DICE GAME)\n")

    print("GAME RULES")
    print("----------")
    print("Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold:")
    print("- If the player rolls a 1, they score nothing and it becomes the next player's turn.")
    print("- If the player rolls any other number, it is added to their turn total and the player's turn continues.")
    print("- If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.")
    print("The first player to score 100 or more points win\n")
    
    number_of_players = input("Enter number of players (1/2): ")

    player1_score = 0
    player2_score = 0
    player_turn = 0

    die = dice.Dice()
    intel = intelligence.Intelligence()

    p1 = player.Player()
    p1.setName(True)

    if number_of_players == "1":
        p2 = player.Player()
        p2.name = "Computer"
        level_of_intelligence = input("\nChoose level of difficulty (1/2): ")

    if number_of_players == "2":
        p2 = player.Player()
        p2.setName(False)


    while p1.score < 100 and p2.score < 100:
        
        print("\n-------------------------")
        print(f"{p1.name if player_turn == 0 else p2.name}'s turn")
        print("-------------------------\n")

        roll = die.roll_dice()
        print(f"Rolling the dice, it was a {roll}")

        if player_turn == 0:

            if roll != 1:
                hold = input(f'({p1.name}) Do you want to hold? (y/n): ')
                
                if hold == "y":
                    player1_score += roll
                    p1.score += player1_score
                    player1_score = 0
                    player_turn = 1
                    print(f'({p1.name}) Total Score : {p1.score}')
                    continue
                else:
                    player1_score += roll
                    print(f'({p1.name}) Current Score : {player1_score}')
                    continue

            else:
                player1_score = 0
                player_turn = 1
                print(f'({p1.name}) Total Score : {p1.score}')
                continue
            
        elif player_turn == 1:

            if number_of_players == "2":
                
                if roll != 1:
                    hold = input(f'({p2.name}) Do you want to hold? (y/n): ')
                    
                    if hold == "y":
                        player2_score += roll
                        p2.score += player2_score
                        player2_score = 0
                        player_turn = 0
                        print(f'({p2.name}) Total Score : {p2.score}')
                        continue
                    else:
                        player2_score += roll
                        print(f'({p2.name}) Current Score : {player2_score}')
                        print(f'({p2.name}) Total Score : {p2.score}')
                        continue
                else:
                    player2_score = 0
                    player_turn = 0
                    print(f'({p2.name}) Total Score : {p2.score}')
                    continue
                
            else:

                if roll != 1:
                    hold = ["y", "n"]
                    index = 0
                    if level_of_intelligence == "1":
                        index = intel.level_1()
                    elif level_of_intelligence == "2":
                        index = intel.level_2()
                    
                    if hold[index] == "y":
                        player2_score += roll
                        p2.score += player2_score
                        player2_score = 0
                        player_turn = 0
                        print(f'({p2.name}) Total Score : {p2.score}')
                        continue
                    else:
                        player2_score += roll
                        print(f'({p2.name}) Current Score : {player2_score}')
                        print(f'({p2.name}) Total Score : {p2.score}')
                        continue
                else:
                    player2_score = 0
                    player_turn = 0
                    print(f'({p2.name}) Total Score : {p2.score}')
                    continue

    else:
        if p1.score >= 100:        
            print(f'\n{p1.name} IS THE WINNER!\n')
        else:
            print(f'\n{p2.name} IS THE WINNER!\n')



if __name__ == "__main__":
    main()
