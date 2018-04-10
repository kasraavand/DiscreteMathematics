from graphs.graph import Graph
import random
graph = Graph()
lowers = "abcdefghijklmnopqrstuvwxyz"
adj = set(random.sample(lowers, random.randint(0, 7)))
for name in lowers:
	graph.add_node(name, 0, **{a:[0, 1] for a in adj - {name}})

print(graph.nodes)
print(graph.edges)