"""unit testing for player class."""

import unittest
from crn.player.player import Player


class TestPlayer(unittest.TestCase):

    def test_init(self):
        """test the player class constructor."""
        player = Player("Alice", False)
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.computer, False)

    def test_is_computer(self):
        """test the is_computer method."""
        player1 = Player("Bob", True)
        player2 = Player("Alice", False)
        self.assertTrue(player1.is_computer())
        self.assertFalse(player2.is_computer())

    def test_fetch_name(self):
        """test the fetch_name method."""
        player = Player("Alice", False)
        self.assertEqual(player.fetch_name(), "Alice")

    def test_update_name(self):
        """test the update_name method."""
        player = Player("Alice", False)
        player.update_name("Bob")
        self.assertEqual(player.name, "Bob")

    def test_update_name_with_non_string(self):
        """test the update_name method when given a non-string value."""
        player = Player("Alice", False)
        player.update_name(123)
        self.assertEqual(player.name, "123")


if __name__ == '__main__':
    unittest.main()
