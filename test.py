from graphs.graph import Graph
from graphs.path import ShortestPath
import random


graph = Graph()
lowers = "abcdefgh"
for name in lowers:
	adj = set(random.sample(lowers, random.randint(0, 7)))
	ne = {a:[round(random.random()*10, 0), 1] for a in adj - {name}}
	graph.add_node(name, 0, **ne)

# print(graph.nodes)
# print(graph.edges)

S = ShortestPath(graph)

S.shortest_path('a', 'e')

print(graph)
print(S.edge_to)
