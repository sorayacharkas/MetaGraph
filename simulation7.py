import matplotlib.pyplot as plt
from numpy import *
import networkx as nx

n = 50
p = 0.34

l = []
for _ in range(100):
    g = nx.gnp_random_graph(n, p)
    l.append(nx.diameter(g))
    
print(sum(l)/len(l))