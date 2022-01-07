import random


class FairRoulette():
    def _init_(self):
        self.pockets = []
        for i in range(1, 37):
            self.ball = None
        self.pocketOdds = len(self.pockets)-1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def betPockets(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else:
            return-amt

    def __str__(self):
        return'Fair Roulette'


print(FairRoulette())
