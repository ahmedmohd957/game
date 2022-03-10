class Player:

    name = ""
    score = 0

    def setName(self, selected_plyr):
        self.name = input(f"\n(Player {selected_plyr}) Enter your name: ")

    def updateName(self):
        self.name = input(f"\n({self.name}) Enter a new name: ")
        print(f"Name successfully changed to {self.name}\n")
