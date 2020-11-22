from collections import Counter
import random


class RPS:
    def __init__(self):
        self.moves = 0
        self.wins = 0
        self.prev = None
        self.answers = {
            0: [],
            1: [],
            2: []
        }

    @staticmethod
    def loses_to(throw: int):
        """0=rock, 1=paper, 2=scissors"""
        match_ups = {
            0: 1,
            1: 2,
            2: 0
        }
        return match_ups[throw]

    @staticmethod
    def wins_with(throw: int):
        """0=rock, 1=paper, 2=scissors"""
        match_ups = {
            0: 2,
            1: 0,
            2: 1
        }
        return match_ups[throw]

    def get_ratio(self) -> float:
        if self.moves < 1:
            return 0
        return self.wins / self.moves

    def get_answer(self, prev) -> int:
        if self.moves < 1:
            self.moves = self.moves + 1
            return random.choice([0, 1, 2])
        answer = self.get_freq(prev)
        wins = self.loses_to(answer)
        self.moves = self.moves + 1
        return wins

    def append_answer(self, current, prev):
        if prev is not None:
            foo = self.answers[prev]
            foo.append(current)

    def get_freq(self, el: int) -> int:
        c = Counter(self.answers[el])
        if len(c.most_common()) < 1:
            return random.choice([0, 1, 2])
        return c.most_common()[0][0]

    def answer(self, answer) -> int:
        parsed = int(answer)
        predicted = self.get_answer(self.prev)
        self.append_answer(parsed, self.prev)
        self.prev = parsed
        self.moves += 1
        if parsed != predicted and self.wins_with(parsed) != predicted:
            self.wins += 1
        return predicted
