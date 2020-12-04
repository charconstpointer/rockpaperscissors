import random


def translate_symbols(i: int) -> str:
    d = {
        0: 'rock',
        1: 'paper',
        2: 'scissors'
    }
    return d[i]


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
        print(row)


def loses_to(i: str) -> str:
    d = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    return d[i]


def chose(row: dict) -> str:
    pop = list(row.keys())[:-1]
    values = list(row.values())
    count = values[len(row) - 1]
    if count == 0:
        return random.choice(pop)
    transitions = values[:-1]
    probability = [el / count for el in transitions]
    next_move = random.choices(weights=probability, population=pop, k=3)
    return loses_to(next_move[0])


def get_score(number: str, choice: str):
    if number is choice:
        return 0
    lt = loses_to(number)
    if choice is lt:
        return -1
    return 1
    # lt = loses_to(choice)
    # if number is lt:
    #
    # return 0


def main():
    a = {'rock': 0, 'paper': 0, 'scissors': 0, 'count': 0}
    b = {'rock': 0, 'paper': 0, 'scissors': 0, 'count': 0}
    c = {'rock': 0, 'paper': 0, 'scissors': 0, 'count': 0}
    rows = [a, b, c]
    prev = None
    games = 0
    points = 0
    while True:
        print_matrix(rows, cols=3)
        ans = input()
        if not str.isnumeric(ans):
            continue

        number = int(ans)
        games += 1

        if -1 < number < 3:
            if prev is None:
                prev = number
            key = translate_symbols(number)
            choice = chose(rows[prev])
            player_choice = translate_symbols(number)
            print("you", player_choice, "vs", choice)
            points += get_score(player_choice, choice)
            print("score", points)
            rows[prev][key] += 1
            rows[prev]['count'] += 1
            prev = number
            continue


if __name__ == '__main__':
    main()
