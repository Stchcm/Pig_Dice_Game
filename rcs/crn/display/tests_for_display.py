"""unit testing for display class."""

import unittest
from unittest.mock import patch
from io import StringIO
from pathlib import Path
from crn.display.display import Display


class TestDisplay(unittest.TestCase):

    def setUp(self):
        self.display = Display()

    def test_assets_path(self):
        """test if the assets_path attribute is correctly set."""
        self.assertEqual(
            self.display.assets_path,
            Path(__file__).parent.joinpath('img')
        )

    @patch('builtins.print')
    def test_displ_header(self, mock_print):
        """test if displ_header calls print with the correct arguments."""
        self.display.displ_header()
        mock_print.assert_called_once()

    @patch('builtins.print')
    def test_displ_intro_img(self, mock_print):
        """test if displ_intro_img calls print with the correct arguments."""
        self.display.displ_intro_img()
        mock_print.assert_called_once()

    @patch('builtins.input', return_value='test_value')
    def test_displ_promt(self, mock_input):
        """test if displ_promt returns the correct input value."""
        result = self.display.displ_promt("Enter a value")
        self.assertEqual(result, 'test_value')
        mock_input.assert_called_once_with("Enter a value -> ")

    @patch('builtins.print')
    def test_displ_intro_menu(self, mock_print):
        """test if displ_intro_menu calls print with the correct arguments."""
        self.display.displ_intro_menu()
        mock_print.assert_called_once()

    @patch('builtins.print')
    def test_displ_computer_menu(self, mock_print):
        """test if displ_computer_menu calls print with the correct arguments."""
        self.display.displ_computer_menu()
        mock_print.assert_called_once()

    @patch('builtins.print')
    def test_displ_realtime_menu(self, mock_print):
        """test if displ_realtime_menu calls print with the correct arguments."""
        self.display.displ_realtime_menu()
        mock_print.assert_called_once()

    @patch('builtins.print')
    def test_displ_rules(self, mock_print):
        """test if displ_rules calls print with the correct arguments."""
        self.display.displ_rules()
        mock_print.assert_called_once()

    @patch('builtins.print')
    def test_displ_dice(self, mock_print):
        """test if displ_dice calls print with the correct arguments."""
        self.display.displ_dice((1, 6))
        mock_print.assert_called_once()

    @patch('builtins.print')
    def test_displ_table(self, mock_print):
        """test if displ_table calls print with the correct arguments."""
        self.display.displ_table([["Player1", 10], ["Player2", 20]])
        mock_print.assert_called_once()

    @patch('builtins.print')
    def test_displ_winner(self, mock_print):
        """test if displ_winner calls print with the correct arguments."""
        self.display.displ_winner("Player1")
        mock_print.assert_called_once()

    @patch('os.system')
    def test_displ_clear(self, mock_os_system):
        """test if displ_clear calls os.system with the correct arguments."""
        self.display.displ_clear()
        mock_os_system.assert_called_once()


if __name__ == '__main__':
    unittest.main()

