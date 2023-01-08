import matplotlib.pyplot as plt
from numpy import *
import networkx as nx

n = 100
p = 0.34



l = []
for _ in range(100):
    g = nx.gnp_random_graph(n, p)
    temp = nx.triangles(g)
    s = 0
    for i in temp:
        s += temp[i]
    s = s // 3
    l.append(s)

print(sum(l)/len(l))