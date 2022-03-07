class Player:
    
    score = 0

    def __init__(self, name):
        self.name = name

    def updateName(self):
        self.name = input("Enter a new name: ")
