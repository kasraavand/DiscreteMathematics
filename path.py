from operator import attrgetter
from functools import lru_cache
from collections import deque


class ShortestPath:
    # Dijkstra
    def __init__(self, *args, **kwargs):
        # Get start and end nodes
        self.graph = args[0]
        __start = kwargs['start']
        self.sart = self.graph[__start]
        __end = kwargs['end']
        self.end = self.graph[__end]
        self.dist_to = {}
        self.edge_to = {}

    def shortest_path(self, start, end):
        for v in self.graph.nodes:
            self.dist_to[v] = float('inf')
        self.dist_to[start] = 0.0
        queue = deque()
        queue.extendleft((0, start))
        while queue:
            self.relax(queue, queue.pop())

    def relax(self, queue, node):
        for n in node.neighbors:
            # edge = self.graph.get_edge(node, n)
            edge = self.graph.get_edge(node, n)
            if self.dist_to[n] > self.dist_to[node] + edge.weight:
                self.dist_to[n] = self.dist_to[node] + edge.weight;
                self.edge_to[n] = edge;
                ind = queue.index(n)
                queue.insert(ind, (n, self.dist_to[n]))

    def create_sp_tree(self):
        # Create the shortest path tree
        # for node in self.graph.node:
        pass
