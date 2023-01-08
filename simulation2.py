import matplotlib.pyplot as plt
from numpy import *
import networkx as nx
n = 1000
p = 0.00016

l = []
for i in range(10):
    g = nx.gnp_random_graph(n, p)
    s = 0
    for i in range(n):
        s += len(g.adj[i])
    s = s // 2
    s = s / n
    num = 0
    for i in range(n):
        if len(g.adj[i]) > s:
            num += 1
    l.append(num)
    
ans = sum(l)/len(l)
print(f'num ejtemayii : {ans}')

g = nx.gnp_random_graph(n, p)
l = []

for i in range(n):
    l.append(len(g.adj[i]))
    
plt.hist(l)
plt.show()