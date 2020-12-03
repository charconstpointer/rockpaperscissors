import math


def print_matrix(m):
    r = math.sqrt(len(m))
    for i, e in enumerate(m):
        if (i + 1) % r == 0:
            print(e)
        else:
            print(e, end=" ")


class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = []
        self.labels = {}

    # self.matrix = [None for _ in range(n)]

    def print_matrix(self):
        for label in self.labels.keys():
            print(label, end="   ")
        print()
        for i, e in enumerate(self.matrix):
            if (i + 1) % self.n == 0:
                print(e)
            else:
                print(e, end=" ")

    def load(self, m, labels: list = None):
        if labels is not None:
            for i, label in enumerate(labels):
                self.labels[label] = i
        self.matrix = m


def main():
    m = [0.0, 0.5, 0.4, 0.0, 1.0, 0.0, 0.6, 0.0, 0.4]
    g = Graph(3)
    g.load(m)
    g.print_matrix()
    
    # print_matrix(m)


if __name__ == '__main__':
    main()
