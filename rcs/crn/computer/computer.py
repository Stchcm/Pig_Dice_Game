"""computer mod to implement concept to control its difficulty."""

from random import shuffle


class Computer:
    """computer class."""

    def __init__(self, diff):
        """constructor for computer class."""
        # diff - difficulty
        # prob - probability
        # b_l - biased list
        # d_l - decision list
        # gen - generate
        self.diff = diff if 0 < diff < 4 else 1
        self.prob = self.set_prob()
        self.b_l = self.gen_b_l()
        self.d_l = self.gen_d_l()

    def get_diff(self):
        """fetch and return computer's difficulty."""
        return self.diff

    def set_diff(self, diff):
        """Change the difficulty of the computer."""
        self.diff = diff

    def set_prob(self):
        """implementing dice sides probability based on difficulty."""
        match self.diff:
            case 1:
                self.prob = (20, 30, 20, 10, 10, 10)
            case 2:
                self.prob = (10, 20, 30, 10, 20, 10)
            case 3:
                self.prob = (10, 10, 10, 30, 20, 20)

        return self.get_prob()

    def get_prob(self):
        """fetch and return dice sides probability."""
        return self.prob

    def gen_b_l(self):
        """generate biased list based on probability."""
        b_l = []
        curr_side = 0
        for i in self.get_prob():
            i = i // 10
            curr_side += 1
            for _ in range(i):
                b_l.append(curr_side)
        shuffle(b_l)
        return b_l

    def get_b_l(self):
        """fetch and return biased list with dice sides."""
        return self.b_l

    def gen_d_l(self):
        """generate decision list to pass or roll based on difficulty."""
        match(self.get_diff()):
            case 1:
                d_l = ["pass", "pass", "roll", "roll", "roll"]
                shuffle(d_l)
                return d_l
            case 2:
                d_l = ["pass", "roll", "roll", "roll", "roll"]
                shuffle(d_l)
                return d_l
            case 3:
                d_l = ["pass", "roll", "roll",
                          "roll", "roll", "roll", "roll"]
                shuffle(d_l)
                return d_l

    def get_d_l(self):
        """fetch and return decision list."""
        return self.d_l
