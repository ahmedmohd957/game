"""This class represents the player."""


class Player:

    name = ""
    score = 0

    def set_name(self, selected_plyr):
        """Sets the name for the player"""
        self.name = input(f"\n(Player {selected_plyr}) Enter your name: ")

    def update_name(self):
        """Updates the name for the player"""
        self.name = input(f"\n({self.name}) Enter a new name: ")
        print(f"Name successfully changed to {self.name}\n")
