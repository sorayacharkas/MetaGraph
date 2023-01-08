import matplotlib.pyplot as plt
from numpy import *
import networkx as nx
n = 1000
p = 0.0033

g = nx.gnp_random_graph(n, p)
l = []

for i in range(n):
    for j in range(i + 1, n):
        try:
            l.append(nx.shortest_path_length(g, source = i, target = j))
        except nx.NetworkXNoPath:
            continue
print(f'expected dist : {sum(l)/len(l)}')