"""display mod to implement decent graphical representation."""

import os
import platform
from pathlib import Path
from textwrap import dedent
import climage
import art
import tabulate


class Display:
    """display Class."""

    def __init__(self):
        """constructor for display class."""
        self.assets_path = (Path(__file__).parent).joinpath('img')

    def displ_header(self):
        """display game name."""
        return print(art.text2art("PIG  DICE  GAME", font="block"))

    def displ_intro_img(self):
        """display game intro image."""
        return print(
            climage.convert(
                f'{self.assets_path}/dice_intro.jpg',
                is_unicode=True,
                width=61,
                palette="RGB"
            )
        )

    def displ_promt(self, text):
        """display a prompt to enable user to input information."""
        value = input(f"{text} -> ")
        return value

    def displ_intro_menu(self):
        """display game intro menu."""
        return print(dedent("""\
                    - Player vs Player | (multiplayer)
                    - Player vs Bot    | (bot)
                    - View game rules  | (rules)
                    - Exit             | (exit)\n"""))

    def displ_computer_menu(self):
        """displaying computer's difficulty menu."""
        return print("1. Easy\n2. Medium\n3. Hard\n")

    def displ_realtime_menu(self):
        """Display a realtime menu when playing."""
        return print(dedent("""\
                    1. Roll
                    2. Pass
                    3. Change/Update name
                    4. Exit current game\n"""))

    def displ_rules(self):
        """displaying rules of the game."""
        return print(dedent("""\
                    Pig Dice Game. Here we have some simple rules,
                    following which guarantees you a pleasant game!\n
                    - Two players can participate in the game, either playing
                    against each other or against computer. During each turn,
                    a player rolls a pair of six-sided dice.\n
                    - Total of the numbers on the dice determines the player's
                    score for the turn.\n
                    - Players have option to roll the dice again and add the
                    resulting sum to their existing score. Alternatively, 
                    they can end their turn and retain their current score.\n
                    - If a player rolls a one either die, their turn concludes
                    and they earn no points for that turn.\n
                    - Rolling a one on both dice results in the player's turn
                    ending the loss of their entire score for the round.\n
                    - The game continues until a player reaches a
                    predetermined victory score(e.g., 100 points).
                    First player to achieve this score wins the game.\n"""))

    def displ_dice(self, sides_tuple):
        """displaying two dices which a player gets."""
        dice1 = climage.convert(
            f'{self.assets_path}/dice_{sides_tuple[0]}.png',
            is_unicode=True,
            is_truecolor=True,
            is_256color=False,
            width=12
        )
        dice2 = climage.convert(
            f'{self.assets_path}/dice_{sides_tuple[1]}.png',
            is_unicode=True,
            is_truecolor=True,
            is_256color=False,
            width=12
        )
        return print(f'{dice1}\n{dice2}')

    def displ_table(self, score_l):
        """displaying a table which keeps track of the scoreboard."""
        table = score_l
        headers = ["Player", "Score"]
        parsed_table = tabulate.tabulate(
            table,
            headers,
            tablefmt="grid"
        )
        return print(f'{parsed_table}\n')

    def displ_winner(self, player_name):
        """displaying game winner."""
        return print(art.text2art(f"{player_name} won the game!\n",
                                  font="block"))

    def displ_clear(self):
        """clearing the display."""
        match (platform.system()):
            case 'Windows' | 'windows':
                return os.system('cls')
            case _:
                return os.system('clear')
