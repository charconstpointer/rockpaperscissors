import random


def translate_symbols(i: int) -> str:
    d = {
        0: 'rock',
        1: 'paper',
        2: 'scissors'
    }
    return d[i]


def translate(i: int):
    d = {
        0: 'a',
        1: 'b',
        2: 'c'
    }
    return d[i]


def translate_str(s: str):
    d = {
        'a': 0,
        'b': 1,
        'c': 2
    }
    return d[s]


def print_matrix(rows: list, cols=3):
    for i, el in enumerate(rows):
        steps = list(el.values())[0:cols]
        count = list(el.values())[cols]
        row = []
        if count == 0:
            row = [0 for _ in range(cols)]
            print(row)
            continue
        for step in steps:
            probability = step / count
            row.append(float("{:.2f}".format(probability)))
            # print("rb", row, probability)
            # row.append(probability)
            # print("ra", row)
            # # print(row, end=" ")
        print(row)


def loses_to(i: int) -> int:
    d = {
        0: 1,
        1: 2,
        2: 0
    }
    return d[i]


def chose(row: dict) -> int:
    pop = list(row.keys())[:-1]
    values = list(row.values())
    count = values[len(row) - 1]
    if count == 0:
        return random.choice(pop)
    transitions = values[:-1]
    probability = [el / count for el in transitions]
    next_move = random.choices(weights=probability, population=pop, k=3)
    return loses_to(translate_str(next_move[0]))


def main():
    a = {'a': 0, 'b': 0, 'c': 0, 'count': 0}
    b = {'a': 0, 'b': 0, 'c': 0, 'count': 0}
    c = {'a': 0, 'b': 0, 'c': 0, 'count': 0}
    rows = [a, b, c]
    prev = None
    while True:
        print_matrix(rows, cols=3)
        ans = input()
        if not str.isnumeric(ans):
            continue
        number = int(ans)
        if prev is None:
            prev = number
            continue
        if -1 < number < 3:
            key = translate(number)
            rows[prev][key] += 1
            rows[prev]['count'] += 1
            c = chose(rows[prev])
            print("you", translate_symbols(number), "vs", translate_symbols(c))
            # print("you :", number, "me", translate_str(c))
            prev = number
            continue

    pass


if __name__ == '__main__':
    main()
