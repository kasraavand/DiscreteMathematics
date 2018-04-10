from uuid import uuid1
from functools import lru_cache


class NodeExist(Exception):
    pass


class Node(Graph):
    def __init__(self, *args):
        self.id = uuid1()
        # name is a hashable unique property of node 
        self.name = args[0]
        self.value = args[1]
        self.neighbors = set()
        self.sorted_neighbors = None

    def add_neigbor(self, node_id):
        self.neighbors.add(node_id)

    def is_neighbor(self, node):
        return node.id in self.neighbors
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, node):
        return self.id is node.id


class Edge:
    def __init__(self, _left, _right, weight=0, direction=True):
        self.left = left
        self.right = right
        self.weight = weight
        # If default direction is set from left to right
        self._direction = direction

    def direction(self, node):
        """
        If direction is 1, return True if we are in left node and False
        otherwise. Else, return True if we are in right node and False
        otherwise.
        """
        if self._direction:
            return node is self.left
        return node is self.right


class Graph:
    def __init__(self, *args, **kwargs):
        self.nodes = {}
        self.edges = {}
        self.string_repr = "graph: {} nodes and {} edges"
 
    def __getitem__(self, name):
        return self.nodes[name]

    def __repr__(self):
        return self.string_repr.format(len(self.nodes),
                                       len(self.edges))
    
    def __str__():
        return self.string_repr.format(len(self.nodes),
                                       len(self.edges))

    def add_node(self, name, value, **adjacents):
        """
        adjacents are keyword args with keys as node names
        and a list of direction and weight of the edge as value
        e.g. node2=[10.5, -1]   
        """
        if name not in self.nodes:
            node = Node(name)
            self.nodes[name] = Node(name)
            for name, (weight, direction) in adjacents.items():
                edge = Edge(node, self.nodes[name], weight=weight, direction=direction)
                self[(node.name, name)] = edge
        else:
            # raise NodeExist
            pass

    def delete_node(self, node):
        self.nodes.remove(node.name)

    def get_edge(self, node_1, node_2):
        return self.edges[(node_1.id, node_2.id)]

    def get_weight(self, node_1, node_2):
        edge = self.get_edge(node_1, node_2)
        return edge.weight

    def get_all_edges(self, node, *neighbors):
        for n in neighbors:
            yield self.get_edge(node, n)

    @lru_cache
    def get_sorted_neighbors(self, node):
        return sorted(node.neighbors, key=lambda n: self.getweight(node, n))
