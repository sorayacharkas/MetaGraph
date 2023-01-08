import matplotlib.pyplot as plt
from numpy import *
import networkx as nx
n = 1000
p = 0.0034
m = 3000

l = []
for i in range(10):
    g = nx.gnp_random_graph(n, p)
    s = 0
    for i in range(n):
        s += len(g.adj[i])
    l.append(s)
    
ans = sum(l)/len(l)
print(l)
print(ans)
print(abs((ans - m)/m))