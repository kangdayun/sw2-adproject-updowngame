import random

class Number:

    def __init__(self):
        self.randomNum = random.randint(0, 999)

    def randomNumber(self):
        return random.randint(0, 999)

    # Set random number in given range
    def rangeNumber(self, start, end):
        if start <= end:
            return random.randint(int(start), int(end))
        return