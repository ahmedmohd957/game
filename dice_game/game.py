import player
import dice
import intelligence

class Game:

    number_of_players = 0
    player1_score = 0
    player2_score = 0
    player_turn = 0
    level_of_intelligence = 0

    p1 = None
    p2 = None

    def start(self):
        self.number_of_players = int(input("\nEnter number of players (1/2): "))

        self.p1 = player.Player()
        self.p1.setName(True)

        if self.number_of_players == 1:
            self.p2 = player.Player()
            self.p2.name = "Computer"
            self.level_of_intelligence = int(input("\nChoose level of difficulty (1/2): "))

        if self.number_of_players == 2:
            self.p2 = player.Player()
            self.p2.setName(False)


    def roll(self):
        die = dice.Dice()
        roll = die.roll_dice()
        print(f"\n{self.p1.name if self.player_turn == 0 else self.p2.name}'s rolling the dice, it was a {roll}")

        if self.player_turn == 0:
            
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


    def computer(self, roll):
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
