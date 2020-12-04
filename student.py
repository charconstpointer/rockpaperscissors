from __future__ import annotations

import random


class State:
    def __init__(self, name: str, state: int):
        self.state = state
        self.name = name
        self.transitions = {}

    def add_transition(self, state: State, p: float):
        self.transitions[state] = p
        pass

    def move(self) -> State:
        proba = list(self.transitions.values())
        next_state = random.choices(population=list(self.transitions.keys()), weights=proba, k=1)
        return next_state[0]


def main():
    s1 = State("dom", 0)
    s2 = State("stolowka", 1)
    s3 = State("klub", 2)
    s4 = State("wydzial", 3)
    """dom->"""
    s1.add_transition(s1, 0.1)
    s1.add_transition(s3, 0.4)
    s1.add_transition(s2, 0.5)
    """stolowka->"""
    s2.add_transition(s1, 0.5)
    s2.add_transition(s4, 0.3)
    s2.add_transition(s2, 0.2)
    """klub->"""
    s3.add_transition(s1, 1)
    """wydzial->"""
    s4.add_transition(s1, 0.4)
    s4.add_transition(s2, 0.3)
    s4.add_transition(s3, 0.3)
    s_new = s1.move()
    states = []
    n = 365 * 6  # every 4hours for a whole year
    for i in range(n):
        s_new = s_new.move()
        if s_new.state == 0:
            states.append(s_new.state)
    print(len(states) / n)


if __name__ == '__main__':
    main()
