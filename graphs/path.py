from operator import attrgetter
from functools import lru_cache
from collections import deque, OrderedDict


class ShortestPath:
    # Dijkstra
    def __init__(self, *args, **kwargs):
        # Get start and end nodes
        self.graph = args[0]
        # __start = kwargs['start']
        # self.start = self.graph[__start]
        # __end = kwargs['end']
        # self.end = self.graph[__end]
        self.dist_to = {}
        self.edge_to = {}
        self.queue = {}

    def shortest_path(self, start, end):
        start, end = self.graph[start], self.graph[end]
        print(start.neighbors)
        for v in self.graph.nodes:
            self.dist_to[v] = float('inf')
        self.dist_to[start.name] = 0.0
        self.queue[start] = 0.0
        while self.queue:
            self.relax(min(self.queue, key=self.queue.get))

    def relax(self, node):
        self.queue.pop(node)
        for n in self.graph.get_sorted_neighbors(node):
            edge = self.graph.get_edge(node, n)
            if self.dist_to[n.name] > self.dist_to[node.name] + edge.weight:
                self.dist_to[n.name] = self.dist_to[node.name] + edge.weight
                self.edge_to[n.name] = edge
                self.queue[n] = self.dist_to[n.name]

    def create_sp_tree(self):
        # Create the shortest path tree
        # for node in self.graph.node:
        pass
