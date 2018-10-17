import random


class Opponent:

    power = -1

    def __init__(self):
        self.power = random.randint(1, 10)

    def getPower(self):
        return self.power