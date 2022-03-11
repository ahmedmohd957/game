"""This class represents the highscore."""
from prettytable import PrettyTable


class HighScore:
    def get_highscore(self, players, current_scores, total_scores):
        """Get the representation of the highscore."""
        columns = ["Players", "Score", "Total"]
        mytable = PrettyTable()
        mytable.add_column(columns[0], players)
        mytable.add_column(columns[1], current_scores)
        mytable.add_column(columns[2], total_scores)
        print(mytable)
