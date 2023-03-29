"""unit testing for dice class."""

import unittest
from crn.dice.dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_init(self):
        """test that the dice constructor initializes a shuffled list of sides."""
        self.assertEqual(len(self.dice.sides), 6)
        self.assertEqual(sorted(self.dice.sides), [1, 2, 3, 4, 5, 6])

    def test_roll_sides(self):
        """test that the roll() method returns a dictionary with a tuple 'cast' containing two random sides."""
        roll_result = self.dice.roll(self.dice.sides)
        self.assertIsInstance(roll_result['cast'], tuple)
        self.assertEqual(len(roll_result['cast']), 2)
        for side in roll_result['cast']:
            self.assertIn(side, self.dice.sides)

    def test_roll_sum(self):
        """test that the roll() method returns a dictionary with an integer 'sum' that is the sum of the 'cast' tuple."""
        roll_result = self.dice.roll(self.dice.sides)
        self.assertIsInstance(roll_result['sum'], int)
        self.assertEqual(roll_result['sum'], sum(roll_result['cast']))

    def test_roll_range(self):
        """test that the roll() method returns a sum within the valid range of 2 to 12."""
        for _ in range(1000):
            roll_result = self.dice.roll(self.dice.sides)
            self.assertGreaterEqual(roll_result['sum'], 2)
            self.assertLessEqual(roll_result['sum'], 12)


if __name__ == '__main__':
    unittest.main()
