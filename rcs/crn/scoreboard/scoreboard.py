"""scoreboard mod."""


class Scoreboard:
    """scoreboard Class."""

    def __init__(self, players_l):
        """creating new high score."""
        self.max_score = 100
        self.winner = None
        self.scores = []
        for player in players_l:
            self.scores.append([player, 0])

    def add_score(self, name, score):
        """adding new score to the list."""
        for i, _ in enumerate(self.scores):
            if name in self.scores[i][0]:
                self.scores[i][1] += score

    def update_name(self, current_name, new_name):
        """updating name for player in scoreboard."""
        for i, _ in enumerate(self.scores):
            if current_name == self.scores[i][0]:
                self.scores[i][0] = new_name

    def clean_score(self, name):
        """resetting score of players."""
        for i, _ in enumerate(self.scores):
            if name in self.scores[i][0]:
                self.scores[i][1] = 0

    def find_winner(self):
        """get the winner."""
        for i, _ in enumerate(self.scores):
            if self.scores[i][1] >= 100:
                self.winner = self.scores[i][0]
                return self.winner
        return None

    def retrieve_player(self, name):
        """player getter."""
        for i, _ in enumerate(self.scores):
            if self.scores[i][0] == name:
                return self.scores[i]
        return None

    def retrieve_scores(self):
        """scores getter."""
        return self.scores
