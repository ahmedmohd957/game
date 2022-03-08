import player
import dice
import intelligence

def main():
    
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
        level_of_intelligence = input("Choose Level (1/2): ")

    if number_of_players == "2":
        p2 = player.Player()
        p2.setName(False)
    
    print(p1.name)
    print(p2.name)


    while p1.score < 100 and p2.score < 100:
        
        print("          ")
        print("-------------------------")
        print(f"   Player {player_turn+1} Turn   ")
        print("-------------------------")
        print("          ")

        roll = die.roll_dice()
        print(roll)

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
                        print("Computer chose hold")
                        player2_score += roll
                        p2.score += player2_score
                        player2_score = 0
                        player_turn = 0
                        print(f'({p2.name}) Total Score : {p2.score}')
                        continue
                    else:
                        print("Computer chose continue")
                        player2_score += roll
                        print(f'({p2.name}) Current Score : {player2_score}')
                        continue
                else:
                    player2_score = 0
                    player_turn = 0
                    print(f'({p2.name}) Total Score : {p2.score}')
                    continue

    else:
        if p1.score >= 100:        
            print(f'{p1.name} is the winner!')
        else:
            print(f'{p2.name} is the winner!')



main()
