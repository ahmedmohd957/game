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
        print("\nNow you're ready to roll the dice\n")
    
    def do_roll(self, _):
        self.game.roll_test()
    
    def do_cheat(self, _):
        print("cheat")

    def do_exit(self, _):
        return True
    
    def do_quit(self, arg):
        return self.do_exit(arg)
    
    def do_q(self, arg):
        return self.do_exit(arg)
