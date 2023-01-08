import matplotlib.pyplot as plt
from numpy import *
import networkx as nx
n = 1000
p = 0.003

g = nx.gnp_random_graph(n, p)


l = []
for i in range(n):
    temp = g.adj[i]
    
    s = 0
    for j in temp:
        for k in temp:
            if j == k:
                continue
            if k in g.adj[j]:
                s += 1
    s = s // 2
    l.append(s)
    
ans = sum(l)/len(l)
print(ans)