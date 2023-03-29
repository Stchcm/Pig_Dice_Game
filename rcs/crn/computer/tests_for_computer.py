"""unit testing for computer class."""

import unittest
from crn.computer.computer import Computer


class TestComputer(unittest.TestCase):
    """testing computer class"""

    def test_difficulty_initialization(self):
        """test if the difficulty is correctly initialized."""
        comp = Computer(2)
        self.assertEqual(comp.get_diff(), 2)

    def test_invalid_difficulty_initialization(self):
        """test if the default difficulty is set when an invalid difficulty value is provided"""
        comp = Computer(5)
        self.assertEqual(comp.get_diff(), 1)

    def test_set_difficulty(self):
        """test if the set_diff method correctly changes the difficulty"""
        comp = Computer(1)
        comp.set_diff(3)
        self.assertEqual(comp.get_diff(), 3)

    def test_set_and_get_prob(self):
        """Test if the set_prob method sets the correct probability values based on the difficulty"""
        comp = Computer(1)
        prob = comp.set_prob()
        self.assertEqual(prob, (20, 30, 20, 10, 10, 10))

    def test_generate_biased_list(self):
        """Test if the gen_b_l method generates a biased list of the correct length and with valid elements"""
        comp = Computer(1)
        b_l = comp.gen_b_l()
        self.assertEqual(len(b_l), 10)
        self.assertTrue(set(b_l).issubset(set(range(1, 7))))

    def test_get_biased_list(self):
        """Test if the get_b_l method returns a biased list of the correct length and with valid elements"""
        comp = Computer(1)
        b_l = comp.get_b_l()
        self.assertEqual(len(b_l), 10)
        self.assertTrue(set(b_l).issubset(set(range(1, 7))))

    def test_generate_decision_list(self):
        """Test if the gen_d_l method generates a decision list of the correct length and with valid elements"""
        comp = Computer(2)
        d_l = comp.gen_d_l()
        self.assertEqual(len(d_l), 5)
        self.assertTrue(set(d_l).issubset(set(["pass", "roll"])))

    def test_get_decision_list(self):
        """Test if the get_d_l method returns a decision list of the correct length and with valid elements"""
        comp = Computer(2)
        d_l = comp.get_d_l()
        self.assertEqual(len(d_l), 5)
        self.assertTrue(set(d_l).issubset(set(["pass", "roll"])))

if __name__ == '__main__':
    unittest.main()
