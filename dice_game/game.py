from multiprocessing.sharedctypes import Value
import player
import dice
import intelligence
import highscore

class Game:

    number_of_players = 1
    player1_score = 0
    player2_score = 0
    player_turn = 0
    level_of_intelligence = 1
    is_cheating = False

    p1 = None
    p2 = None

    def start(self):
        try:
            self.number_of_players = int(input("\nEnter number of players (1/2): "))
            if self.number_of_players < 1 or self.number_of_players > 2:
                raise ValueError

            if self.number_of_players == 1:
                self.level_of_intelligence = int(input("\nChoose level of difficulty (1/2): "))
                if self.level_of_intelligence < 1 or self.level_of_intelligence > 2:
                    raise ValueError
        except ValueError:
            raise ValueError("Choose between '1' or '2'. Start the game again.")

        self.p1 = player.Player()
        self.p1.setName(1)

        self.p2 = player.Player()
        if self.number_of_players == 2:
            self.p2.setName(2)
        else:
            self.p2.name = "Computer"
        
        if self.p1.name == "" or self.p2.name == "":
            raise ValueError("Name cannot be empty. Start the game again.")


    def roll(self):
        die = dice.Dice()
        roll = die.roll_dice()

        if self.player_turn == 0:
            print(f"\n{self.p1.name}'s rolling the dice, it was a {roll}")
            if roll != 1:
                hold = input(f'({self.p1.name}) Do you want to hold? (y/n): ')
                if hold == "y":
                    self.hold(roll)
                    if self.number_of_players == 1 and self.score_below_100():
                        self.roll()
                else:
                    self.player1_score += roll
                    print(f'({self.p1.name}) Score : {self.player1_score}\n')
            else:
                self.player1_score = 0
                self.player_turn = 1
                print(f'({self.p1.name}) Total score : {self.p1.score}\n')
                
                if self.number_of_players == 1 and self.score_below_100():
                    self.roll()
        elif self.player_turn == 1:
            if self.number_of_players == 1:
                self.computer(roll)
            else:
                print(f"\n{self.p2.name}'s rolling the dice, it was a {roll}")
                if roll != 1:
                    hold = input(f'({self.p2.name}) Do you want to hold? (y/n): ')
                    if hold == "y":
                        self.hold(roll)
                    else:
                        self.player2_score += roll
                        print(f'({self.p2.name}) Score : {self.player2_score}\n')
                else:
                    self.player2_score = 0
                    self.player_turn = 0
                    print(f'({self.p2.name}) Total score : {self.p2.score}\n')



    def test(self, roll):
        if self.player_turn == 1 and self.number_of_players == 1:
            self.computer(roll)
            return

        if roll != 1:
            hold = input(f'Do you want to hold? (y/n): ')
            if hold == "y":
                self.hold(roll)
                if self.player_turn == 0 and self.number_of_players == 1:
                    if self.score_below_100():
                        self.roll()
            else:
                if self.player_turn == 0:
                    self.player1_score += roll
                    print(f'({self.p1.name}) Score : {self.player1_score}\n')
                else:
                    self.player2_score += roll
                    print(f'({self.p2.name}) Score : {self.player2_score}\n')
        else:
            if self.player_turn == 0:
                self.player1_score = 0
                self.player_turn = 1
                print(f'({self.p1.name}) Total score : {self.p1.score}\n')
                if self.number_of_players == 1 and self.score_below_100():
                    self.roll()
            else:
                self.player2_score = 0
                self.player_turn = 0
                print(f'({self.p2.name}) Total score : {self.p2.score}\n')
            


    
    def computer(self, roll):
        if self.is_cheating:
            roll = 1
            self.is_cheating = False

        print(f"\n{self.p2.name}'s rolling the dice, it was a {roll}")

        if roll != 1:
            hold = ["y", "n", "n"]
            index = 0
            
            intel = intelligence.Intelligence()
            if self.level_of_intelligence == 1:
                index = intel.level_1()
            elif self.level_of_intelligence == 2:
                index = intel.level_2()
            
            if hold[index] == "y":
                print('Computer chose to "hold"')
                self.hold(roll)
            else:
                self.player2_score += roll
                print('Computer chose to "continue"')
                print(f'({self.p2.name}) Score : {self.player2_score}\n')
                self.roll()
        else:
            self.player2_score = 0
            self.player_turn = 0
            print(f'({self.p2.name}) Total score : {self.p2.score}\n')


    def hold(self, roll):
        if self.player_turn == 0:
            self.player1_score += roll
            self.p1.score += self.player1_score
            self.player1_score = 0
            self.player_turn = 1
            print(f'({self.p1.name}) Total score : {self.p1.score}\n')
        else:
            self.player2_score += roll
            self.p2.score += self.player2_score
            self.player2_score = 0
            self.player_turn = 0
            print(f'({self.p2.name}) Total score : {self.p2.score}\n')


    def score_below_100(self):
        if self.p1.score < 100 and self.p2.score < 100:
            return True
        else:
            return False


    def get_winner(self):
        if self.p1.score >= 100:
            return self.p1.name
        else:
            return self.p2.name
    

    def change_player_name(self):
        if self.p1 and self.p2:
            if self.number_of_players == 1:
                self.p1.updateName()
            else:
                plyr = int(input("Choose player (1/2): "))
                if plyr == 1:
                    self.p1.updateName()
                else:
                    self.p2.updateName()
        else:
            print("You haven't started the game yet!\n")


    def change_game_level(self):
        if self.p1 and self.p2:
            if self.number_of_players == 1:
                print(f"Current level is {self.level_of_intelligence}.")
                val = input("Do you wish to change the  level? (y/n): ")
                if val == "y":
                    self.level_of_intelligence = int(input("\nChoose level of difficulty (1/2): "))
                    print(f"Level of difficulty successfully changed to {self.level_of_intelligence}.\n")
            else:
                print("This setting is only configurable when playing towards a computer!\n")
        else:
            print("You haven't started the game yet!\n")


    def get_highscore(self):
        if self.p1 and self.p2:
            h_score = highscore.HighScore()
            players = [self.p1.name, self.p2.name]
            current_scores = [self.player1_score, self.player2_score]
            total_scores = [self.p1.score, self.p2.score]
            h_score.get_highScore(players, current_scores, total_scores)
        else:
            print("You haven't started the game yet!\n")

    
    def cheat(self):
        if self.p1 and self.p2:
            if self.number_of_players == 2:
                print("Cheating is only available when you're playing against a computer.\n")
                return
            self.is_cheating = True
            print("Cheating... Computer will get a \"1\" in the next round.\n")
        else:
            print("You haven't started the game yet!\n")
