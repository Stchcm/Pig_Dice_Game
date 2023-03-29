"""dice module."""

import random


class Dice:
    """class for six sided dice."""

    def __init__(self):
        """constructor for the class dice."""
        sides = [1, 2, 3, 4, 5, 6]
        random.shuffle(sides)
        self.sides = sides

    def roll(self, sides_l):
        # sides_l - sides/faces list
        """roll."""
        cast = (random.choice(sides_l), random.choice(sides_l))
        sum_cast = cast[0] + cast[1]
        return {'cast': cast, 'sum': sum_cast}
