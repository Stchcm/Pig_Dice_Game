"""player mod."""


class Player:
    """player class."""

    def __init__(self, name, computer):
        """init constructor for player class."""
        self.name = str(name)
        self.computer = computer

    def is_computer(self):
        """checking whether a player is a computer or not. returning bool."""
        return self.computer

    def fetch_name(self):
        """return current name of the player."""
        return self.name

    def update_name(self, name):
        """set new name for the player."""
        self.name = str(name)
