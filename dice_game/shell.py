import cmd
import game

class Shell(cmd.Cmd):
    intro = "Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        super().__init__()
        self.game = game.Game()
    
    def do_start(self, _):
        self.game.start()
        print("\nNow you're ready to roll the dice")
        print("Enter \"roll\" to roll the dice.\n")
    
    def do_roll(self, _):
        self.game.roll()
        if self.game.score_below_100() is not True:
            print(f'{self.game.get_winner()} is the winner!!!')
    
    def do_cheat(self, _):
        self.game.cheat()
    
    def do_score(self, _):
        self.game.get_highscore()

    def do_change_level(self, _):
        self.game.change_game_level()
    
    def do_change_name(self, _):
        self.game.change_player_name()

    def do_exit(self, _):
        return True
    
    def do_quit(self, arg):
        return self.do_exit(arg)
    
    def do_q(self, arg):
        return self.do_exit(arg)
