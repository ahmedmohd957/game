class Player:

    name = ""
    score = 0

    def setName(self, selected_plyr):
        """Sets the name for the player"""
        self.name = input(f"\n(Player {selected_plyr}) Enter your name: ")

    def updateName(self):
        """Updates the name for the player"""
        self.name = input(f"\n({self.name}) Enter a new name: ")
        print(f"Name successfully changed to {self.name}\n")
