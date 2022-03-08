class Player:

    name = ""
    score = 0

    def setName(self):
        self.name = input("Enter your name: ")

    def updateName(self):
        self.name = input("Enter a new name: ")
