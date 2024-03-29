"""This class represents the game."""

import player
import dice
import intelligence
import highscore


class Game:

    # class variable shared by all instances
    number_of_players = 1
    player1_score = 0
    player2_score = 0
    player_turn = 0
    level_of_intelligence = 1
    is_cheating = False
    p_1 = None
    p_2 = None

    def start(self):
        """Starts the game"""
        try:
            self.number_of_players = int(input("\nEnter number of players (1/2): "))
            if self.number_of_players < 1 or self.number_of_players > 2:
                raise ValueError

            if self.number_of_players == 1:
                self.level_of_intelligence = int(
                    input("\nChoose level of difficulty (1/2): ")
                )
                if self.level_of_intelligence < 1 or self.level_of_intelligence > 2:
                    raise ValueError
        except ValueError:
            raise ValueError("Choose between '1' or '2'. Start the game again.")

        self.p_1 = player.Player()
        self.p_1.set_name(1)

        self.p_2 = player.Player()
        if self.number_of_players == 2:
            self.p_2.set_name(2)
        else:
            self.p_2.name = "Computer"

        if self.p_1.name == "" or self.p_2.name == "":
            raise ValueError("Name cannot be empty. Start the game again.")

    def roll(self):
        """Player rolls the dice and chooses wheather to hold or continue."""
        die = dice.Dice()
        roll = die.roll_dice()

        if self.computer_turn() and self.is_cheating:
            roll = 1
            self.is_cheating = False

        if self.player_1_turn():
            print(f"\n{self.p_1.name}'s rolling the dice, it was a {roll}")
        else:
            print(f"\n{self.p_2.name}'s rolling the dice, it was a {roll}")

        if self.computer_turn():
            self.computer(roll)
            return

        if roll != 1:
            hold = input("Do you want to hold? (y/n): ")
            if hold == "y":
                self.hold(roll)
                if self.one_player() and self.score_below_100():
                    self.roll()
            else:
                if self.player_1_turn():
                    self.player1_score += roll
                    print(f"({self.p_1.name}) Score : {self.player1_score}\n")
                else:
                    self.player2_score += roll
                    print(f"({self.p_2.name}) Score : {self.player2_score}\n")
        else:
            if self.player_1_turn():
                self.player1_score = 0
                self.player_turn = 1
                print(f"({self.p_1.name}) Total score : {self.p_1.score}\n")
                if self.one_player() and self.score_below_100():
                    self.roll()
            else:
                self.player2_score = 0
                self.player_turn = 0
                print(f"({self.p_2.name}) Total score : {self.p_2.score}\n")

    def computer(self, roll):
        """Computer's turn to play"""
        if roll != 1:
            intel = intelligence.Intelligence()
            if self.level_of_intelligence == 1:
                hold_or_cont = intel.level_1()
            elif self.level_of_intelligence == 2:
                hold_or_cont = intel.level_2()

            if hold_or_cont == "y":
                print('Computer chose to "hold"')
                self.hold(roll)
            else:
                self.player2_score += roll
                print('Computer chose to "continue"')
                print(f"({self.p_2.name}) Score : {self.player2_score}\n")
                self.roll()
        else:
            self.player2_score = 0
            self.player_turn = 0
            print(f"({self.p_2.name}) Total score : {self.p_2.score}\n")

    def hold(self, roll):
        """Hold the rolled die."""
        if self.player_turn == 0:
            self.player1_score += roll
            self.p_1.score += self.player1_score
            self.player1_score = 0
            self.player_turn = 1
            print(f"({self.p_1.name}) Total score : {self.p_1.score}\n")
        else:
            self.player2_score += roll
            self.p_2.score += self.player2_score
            self.player2_score = 0
            self.player_turn = 0
            print(f"({self.p_2.name}) Total score : {self.p_2.score}\n")

    def player_1_turn(self):
        """Returns if current player is Player 1."""
        return self.player_turn == 0

    def player_2_turn(self):
        """Returns if current player is Player 2."""
        return self.player_turn == 1

    def one_player(self):
        """Returns if the game is played by 1 player."""
        return self.number_of_players == 1

    def computer_turn(self):
        """Return if it's computer's turn."""
        return self.player_2_turn() and self.one_player()

    def score_below_100(self):
        """Checks if score is under 100"""
        if self.p_1.score < 100 and self.p_2.score < 100:
            return True

        return False

    def get_winner(self):
        """Return the name of the winner player."""
        if self.p_1.score >= 100:
            return self.p_1.name

        return self.p_2.name

    def change_player_name(self):
        """Changed the name of the chosen player."""
        if self.p_1 and self.p_2:
            if self.number_of_players == 1:
                self.p_1.update_name()
            else:
                plyr = int(input("Choose player (1/2): "))
                if plyr == 1:
                    self.p_1.update_name()
                else:
                    self.p_2.update_name()
        else:
            print("You haven't started the game yet!\n")

    def change_game_level(self):
        """Changes the games level of intelligence"""
        if self.p_1 and self.p_2:
            if self.number_of_players == 1:
                print(f"Current level is {self.level_of_intelligence}.")
                val = input("Do you wish to change the  level? (y/n): ")
                if val == "y":
                    self.level_of_intelligence = int(
                        input("\nChoose level of difficulty (1/2): ")
                    )
                    print(
                        f"Level successfully changed to {self.level_of_intelligence}.\n"
                    )
            else:
                print(
                    "This setting is only configurable when playing towards a computer!\n"
                )
        else:
            print("You haven't started the game yet!\n")

    def get_highscore(self):
        """Represents the highscore of the current game."""
        if self.p_1 and self.p_2:
            h_score = highscore.HighScore()
            players = [self.p_1.name, self.p_2.name]
            current_scores = [self.player1_score, self.player2_score]
            total_scores = [self.p_1.score, self.p_2.score]
            h_score.get_highscore(players, current_scores, total_scores)
        else:
            print("You haven't started the game yet!\n")

    def cheat(self):
        """Activates cheat"""
        if self.p_1 and self.p_2:
            if self.number_of_players == 2:
                print(
                    "Cheating is only available when you're playing against a computer.\n"
                )
                return
            self.is_cheating = True
            print('Cheating... Computer will get a "1" in the next round.\n')
        else:
            print("You haven't started the game yet!\n")
