import matplotlib.pyplot as plt
from numpy import *
import networkx as nx

c = [] # true, false for connected
l = [] # num no friends

n = 150
p = 0.2

for _ in range(100):
    g = nx.gnp_random_graph(n, p)
    
    c.append(nx.is_connected(g))
    
    num = 0
    for i in range(n):
        if len(g.adj[i]) == 0:
            num += 1
    l.append(num)
    
print(f'prob. connected : {sum(c)/len(c)}')
print(f'prob. tanha : {sum(l)/(len(l)*n)}')