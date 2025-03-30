import functools

@functools.total_ordering
class Node:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost