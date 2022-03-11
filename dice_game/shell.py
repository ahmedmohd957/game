import cmd
import game

class Shell(cmd.Cmd):
    intro = "Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        """initializes the object"""
        super().__init__()
        self.game = game.Game()
    
    def do_start(self, _):
        """Start the game."""
        try:
            self.game.start()
            print("\nNow you're ready to roll the dice")
            print("Enter \"roll\" to roll the dice.\n")
        except ValueError as err:
            print(err)
    
    def do_roll(self, _):
        """Player rolls the dice."""
        self.game.roll()
        if self.game.score_below_100() is not True:
            print(f'{self.game.get_winner()} is the winner!!!')
    
    def do_cheat(self, _):
        """Player activates cheat."""
        self.game.cheat()
    
    def do_score(self, _):
        """Represents the highscore for the current game."""
        self.game.get_highscore()

    def do_change_level(self, _):
        """Changes the level of difficulty of the game."""
        self.game.change_game_level()
    
    def do_change_name(self, _):
        """Changes the name of the selected player."""
        self.game.change_player_name()

    def do_exit(self, _):
        """Leave the game."""
        return True
    
    def do_quit(self, arg):
        """Leave the game."""
        return self.do_exit(arg)
    
    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)
