from operator import attrgetter


class ShortestPath:
    # Dijkstra
    def __init__(self, *args, **kwargs):
        # Get start and end nodes
        self.graph = args[0]
        __start = kwargs['start']
        self.sart = self.graph[__start]
        __end = kwargs['end'] 
        self.end = self.graph[__end]

    def create_tree(self):
        to_node = {}
        while True:
            start_neighbors = self.start.neighbors
            to_node = {edge.right.name: edge.weight for edge in edges}
            for edge in edges:
                for n in node.neighbors:
                    to_node[n.name] = to_node[node.name]
