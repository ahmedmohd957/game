from dis import pretty_flags
from prettytable import PrettyTable


class HighScore ():
    columns = ['Players', 'Score', "total"],
    mytable = PrettyTable()
    mytable.add_column(columns[0], "Ahmed", "Murwan")
    mytable.add_column(columns[1], "25", "40")
    print(mytable)
