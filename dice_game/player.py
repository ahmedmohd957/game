class Player:

    name = ""
    score = 0

    def setName(self, isPlayer_1):
        if isPlayer_1:
            self.name = input("\n(Player 1) Enter your name: ")
        else:
            self.name = input("(Player 2) Enter your name: ")

    def updateName(self):
        self.name = input(f"\n({self.name}) Enter a new name: ")
        print(f"Name successfully changed to {self.name}")
