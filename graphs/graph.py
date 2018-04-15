from uuid import uuid1
from functools import lru_cache
from operator import itemgetter


class NodeExist(Exception):
    pass


class Node():
    def __init__(self, *args):
        self.id = uuid1()
        # name is a hashable unique property of node 
        self.name = args[0]
        self.value = args[1]
        self.neighbors = set()

    def add_neigbor(self, node_name):
        self.neighbors.add(node_name)

    def is_neighbor(self, node):
        return node.id in self.neighbors
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, node):
        return self.id is node.id
    
    def __str__(self):
        return f"Node object: {self.name}"
    
    def __iter__(self):
        return iter([self])


class Edge:
    def __init__(self, _left, _right, weight=0, direction=True):
        self.left = _left
        self.right = _right
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
    
    def __str__(self):
        return str({n: val.neighbors for n, val in self.nodes.items()})

    def add_node(self, name, value, **adjacents):
        """
        adjacents are keyword args with keys as node names
        and a list of direction and weight of the edge as value
        e.g. node2=[10.5, -1]   
        """
        if name not in self.nodes:
            node = Node(name, value)
            self.nodes[name] = node
            for ne, (weight, direction) in adjacents.items():
                try:
                    adj = self.nodes[ne]
                except KeyError:
                    self.nodes[ne] = adj = Node(ne, weight)
                adj.add_neigbor(name)
                node.add_neigbor(ne)
                try:
                    edge = self.edges[(node.name, ne)]
                except KeyError:
                    edge = Edge(node, adj, weight=weight, direction=direction)
                    self.edges[(node.name, ne)] = edge
                
                else:
                    if direction == edge.direction:
                        raise Exception("Mismatch between dierctions for Edge ({}, {})".format(node.name, name))
                    else:
                        edge.direction = 0

        else:
            # raise NodeExist
            pass

    def delete_node(self, node):
        self.nodes.remove(node.name)

    def get_edge(self, node_1, node_2):
        try:
            return self.edges[(node_1.name, node_2.name)]
        except:
            return self.edges[(node_2.name, node_1.name)]
    def get_weight(self, node_1, node_2):
        edge = self.get_edge(node_1, node_2)
        return edge.weight

    def get_all_edges(self, node, *neighbors):
        for n in neighbors:
            yield self.get_edge(node, n)

    @lru_cache(None)
    def get_sorted_neighbors(self, node):
        snids = sorted(node.neighbors, key=lambda n: self.get_weight(node, self.nodes[n]))
        try:
            return itemgetter(*snids)(self.nodes)
        except TypeError:
            return []