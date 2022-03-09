from dis import pretty_flags
from prettytable import PrettyTable


def highScore():
    columns = ['Players', 'Score', 'Total']
    mytable = PrettyTable()
    mytable.add_column(columns[0], ["Ahmed", "Murwan"])
    mytable.add_column(columns[1], ["25", "40"])
    mytable.add_column(columns[2], ["25", "40"])
    print(mytable)

highScore()
