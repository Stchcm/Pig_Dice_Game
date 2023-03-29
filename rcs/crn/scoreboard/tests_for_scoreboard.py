"""unit testing for scoreboard class."""

import unittest
from crn.scoreboard.scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):

    def test_init(self):
        """test if the Scoreboard is initialized correctly."""
        sb = Scoreboard(['Alice', 'Bob'])
        self.assertEqual(sb.scores, [['Alice', 0], ['Bob', 0]])

    def test_add_score(self):
        """test if scores are added correctly."""
        sb = Scoreboard(['Alice', 'Bob'])
        sb.add_score('Alice', 10)
        self.assertEqual(sb.scores, [['Alice', 10], ['Bob', 0]])

    def test_update_name(self):
        """test if player names are updated correctly."""
        sb = Scoreboard(['Alice', 'Bob'])
        sb.update_name('Alice', 'Eve')
        self.assertEqual(sb.scores, [['Eve', 0], ['Bob', 0]])

    def test_clean_score(self):
        """test if scores are reset correctly."""
        sb = Scoreboard(['Alice', 'Bob'])
        sb.add_score('Alice', 10)
        sb.clean_score('Alice')
        self.assertEqual(sb.scores, [['Alice', 0], ['Bob', 0]])

    def test_find_winner(self):
        """test if the winner is found correctly."""
        sb = Scoreboard(['Alice', 'Bob'])
        sb.add_score('Alice', 100)
        self.assertEqual(sb.find_winner(), 'Alice')

    def test_find_winner_no_winner(self):
        """test if the function returns None when there's no winner."""
        sb = Scoreboard(['Alice', 'Bob'])
        self.assertIsNone(sb.find_winner())

    def test_retrieve_player(self):
        """test if player is retrieved correctly."""
        sb = Scoreboard(['Alice', 'Bob'])
        self.assertEqual(sb.retrieve_player('Alice'), ['Alice', 0])

    def test_retrieve_player_not_found(self):
        """test if the function returns None when the player is not found."""
        sb = Scoreboard(['Alice', 'Bob'])
        self.assertIsNone(sb.retrieve_player('Eve'))

    def test_retrieve_scores(self):
        """test if scores are retrieved correctly."""
        sb = Scoreboard(['Alice', 'Bob'])
        sb.add_score('Alice', 10)
        self.assertEqual(sb.retrieve_scores(), [['Alice', 10], ['Bob', 0]])

if __name__ == '__main__':
    unittest.main()
