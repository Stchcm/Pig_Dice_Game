
"""Main module to implement the logic of the game."""

# pylint: disable=import-error
import random
import time
from textwrap import dedent
from cmd import Cmd
from computer.computer import Computer
from dice.dice import Dice
from player.player import Player
from scoreboard.scoreboard import Scoreboard
from display.display import Display

# for global usage
display = Display()


class Main(Cmd):
    """main class."""

    prompt = " -> "

    def preloop(self):
        """runs after starting cmdloop."""
        show_welcome_info()

    def multpl(self, _):
        # multpl - multiplayer
        """invoking a player vs player game."""
        pl1, pl2 = create_players(True)
        scoreboard, dice = i_game(pl1, pl2)

        # clearing terminal for better experience
        display.displ_clear()  # clear terminal for better experience

        # keeping track of turns, pl1 = 1, pl2 = 2
        track = 1
        while not scoreboard.find_winner():  # game round loop
            display.displ_table(scoreboard.retrieve_scores())
            display.displ_realtime_menu()

            if track == 1:
                print(f"It's {pl1.fetch_name()}'s turn\n")
            else:
                print(f"It's {pl2.fetch_name()}'s turn\n")

            choice = val_option("Choose an option -> ", "Invalid option!")

            # logic based on option
            match(choice):
                case 1:
                    display.displ_clear()

                    cast, sum_score = dice.roll(dice.sides).values()
                    display.displ_dice(cast)  # displaying dice

                    if track == 1:  # if it's pl1 turn

                        if (cast[0] == 1) and (cast[1] == 1):
                            scoreboard.clean_score(
                                pl1.fetch_name())
                            track = 2  # gives turn to pl2
                            continue

                        if (cast[0] == 1) or (cast[1] == 1):
                            track = 2
                            continue

                        scoreboard.add_score(
                            pl1.fetch_name(), sum_score)
                    else:  # if it's pl2 turn

                        if (cast[0] == 1) and (cast[1] == 1):
                            scoreboard.clean_score(pl2.fetch_name())
                            track = 1  # give turn to pl1
                            continue

                        if (cast[0] == 1) or (cast[1] == 1):
                            track = 1
                            continue

                        scoreboard.add_score(
                            pl2.fetch_name(), sum_score)
                case 2:
                    display.displ_clear()

                    if track == 1:
                        track = 2
                        continue

                    track = 1
                    continue

                case 3:
                    new_name = val_name(
                        "Enter a new name: ",
                        "Name is too short or already used",
                        scoreboard)

                    if track == 1:  # change pl1 name
                        scoreboard.update_name(
                            pl1.fetch_name(), new_name)
                        pl1.update_name(new_name)

                    if track == 2:  # change pl2 name
                        scoreboard.update_name(
                            pl2.fetch_name(), new_name)
                        pl2.update_name(new_name)

                    display.displ_clear()
                case 4:
                    break

        end_game(scoreboard)  # finish game

    def computer_mod(self, _):
        """invoking player vs computer game."""
        pl1, pl2 = create_players(False)
        scoreboard, dice = i_game(pl1, pl2)

        display.displ_clear()

        display.displ_computer_menu()
        difficulty = val_option(
            "Choose computer's difficulty -> ", "Invalid option!")

        computer = Computer(difficulty)  # create computer
        display.displ_clear()

        track = 1  # keep track of turns, player = 1, computer = 2
        while not scoreboard.find_winner():  # game round loop
            display.displ_table(scoreboard.retrieve_scores())
            display.displ_realtime_menu()

            if track == 2:  # if it's the computer's turn
                display.displ_clear()
                print(f"{pl2.fetch_name()} turn")

                # decide whether to roll or pass
                computer_decision = random.choice(computer.get_d_l())

                if computer_decision == "roll":  # if computer rolls

                    print(f"{pl2.fetch_name()} chose to roll!\n")
                    cast, sum_score = dice.roll(computer.get_b_l()).values()

                    display.displ_dice(cast)

                    if (cast[0] == 1) and (cast[1] == 1):
                        scoreboard.clean_score(pl2.fetch_name())
                        track = 1
                        print(
                            f"{pl2.fetch_name()} lost the entire score :(\n")
                        time.sleep(4)  # improves game flow
                        display.displ_clear()
                        continue

                    if (cast[0] == 1) or (cast[1] == 1):
                        track = 1
                        print(f"{pl2.fetch_name()} lost their turn :/\n")
                        time.sleep(4)
                        display.displ_clear()
                        continue

                    scoreboard.add_score(
                        pl2.fetch_name(), sum_score)
                    display.displ_table(scoreboard.retrieve_scores())
                    time.sleep(4)
                    continue

                else:  # if computer passes
                    print(f"{pl2.fetch_name()} chose to pass..\n")
                    track = 1
                    time.sleep(2)
                    display.displ_clear()
                    continue
            else:  # if it's the player's turn
                print("It's your turn!\n")
                choice = val_option(
                    "Choose an option -> ", "Invalid option!")

                match(choice):  # logic based on option
                    case 1:
                        display.displ_clear()

                        cast, sum_score = dice.roll(dice.sides).values()
                        display.displ_dice(cast)

                        if track == 1:

                            if (cast[0] == 1) and (cast[1] == 1):
                                scoreboard.clean_score(pl1.fetch_name())
                                print("You lost your entire score :(")
                                track = 2
                                time.sleep(4)
                                continue

                            if (cast[0] == 1) or (cast[1] == 1):
                                print("You lost your turn and its score :/")
                                track = 2
                                time.sleep(4)
                                continue

                            scoreboard.add_score(
                                pl1.fetch_name(), sum_score)
                    case 2:
                        if track == 1:
                            track = 2
                            continue
                    case 3:
                        new_name = val_name(
                            "Enter a new name: ",
                            "Name is too short or already used",
                            scoreboard)

                        if track == 1:
                            scoreboard.update_name(
                                pl1.fetch_name(), new_name)
                            pl1.update_name(new_name)

                        display.displ_clear()

                    case 4:
                        break

        end_game(scoreboard)

    def rules(self, _):
        """displaying game rules."""
        display.displ_rules()

    def credits(self, _):
        """displaying project credits."""
        print(dedent("""\n
            This game project was made by:
            Mariam Petrosian & Helmer Scheele\n
            """))

    def exit(self, _):
        """exiting game."""
        print("See you later!\n")
        return True


def show_welcome_info():
    """display game intro."""
    display.displ_clear()
    display.displ_header()
    display.displ_intro_img()
    print("Welcome to Pig Dice!\n")
    display.displ_intro_menu()
    print("Type 'help' to see available commands.\n")


def val_option(prompt, error):
    """validating inputted int."""
    while True:
        try:
            choice = int(input(prompt))
            if "difficulty" not in prompt:  # for in-game menu
                if not 0 < choice < 5:
                    raise ValueError
                return choice

            if not 0 < choice < 4:  # for choosing computer's difficulty
                raise ValueError
            return choice

        except ValueError:
            print(error)
            continue


def val_name(prompt, error, scoreboard):
    """validating name before changing it."""
    # f_names - forbidden names
    f_names = ["Kiki (computer)", "Tori (computer)",
                       "David (computer)", "Mimi (computer)"]  # used by computer
    while True:
        name = str(input(prompt))
        if not scoreboard:  # when creating new players
            if (len(name) < 1) or (name in f_names):
                print(error)
                continue
        else:  # when changing name during game
            if (len(name) < 1 or scoreboard.get_player(name) or
                    name in f_names):
                print(error)
                continue
        return name


def create_players(is_multiplayer):
    """creating players for the game."""
    if is_multiplayer:  # player vs player
        pl1_name = val_name(
            "Enter your name (Player 1): ",
            "Name too short",
            scoreboard=False)

        while True:  # validates it's not same as player1 name
            pl2_name = val_name(
                "Enter your name (Player 2): ",
                "Name too short or already used",
                scoreboard=False)

            if pl1_name == pl2_name:
                print("Name can't be the same for both players.")
                continue
            break

        pl1 = Player(pl1_name, False)
        pl2 = Player(pl2_name, False)
        return pl1, pl2

    else:  # player vs computer
        pl1_name = val_name(
            "Enter your name (Player 1): ",
            "Name too short or can't be used",
            scoreboard=False)

        pl2_name = random.choice(
            ["Kiki (computer)", "Tori (bot)", "David (bot)", "Mimi (bot)"])

        pl1 = Player(pl1_name, False)
        pl2 = Player(pl2_name, True)
        return pl1, pl2


def i_game(pl1, pl2):
    """init game by creating scoreboard and dice objects."""
    scoreboard = Scoreboard([pl1.get_name(), pl2.get_name()])
    dice = Dice()
    return scoreboard, dice


def end_game(scoreboard):
    """End game and show winner."""
    if scoreboard.find_winner():
        display.displ_clear()
        display.displ_winner(scoreboard.find_winner())
        display.displ_table(scoreboard.retrieve_scores())


if __name__ == '__main__':
    Main().cmdloop()
