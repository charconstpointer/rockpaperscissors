from __future__ import annotations

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)

    def bfs(self, start: int):
        visited = [False for _ in self.graph.keys()]
        queue = [start]
        visited[start] = True
        while queue:
            s = queue.pop(0)
            print(s,end="")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


class Node:
    pass


def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5,4)
    g.add_edge(0, 3)
    g.bfs(0)
    pass


if __name__ == '__main__':
    main()
