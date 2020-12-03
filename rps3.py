class Graph:
    pass


def translate(i: int):
    d = {
        0: 'a',
        1: 'b',
        2: 'c'
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
            # print("rb", row, probability)
            # row.append(probability)
            # print("ra", row)
            # # print(row, end=" ")
        print(row)


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
            print(prev)
            key = translate(number)
            print(prev)
            rows[prev][key] += 1
            rows[prev]['count'] += 1
            prev = number
            continue

    pass


if __name__ == '__main__':
    main()
