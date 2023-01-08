import matplotlib.pyplot as plt
from numpy import *
import networkx as nx

def get_mean(n, p):
    

    l = []
    for _ in range(100):
        g = nx.gnp_random_graph(n, p)
        temp = nx.triangles(g)
        s = 0
        for i in temp:
            s += temp[i]
        s = s // 3
        l.append(s)

    return sum(l)/len(l)

n = []
for i in range(10, 101, 10):
    n.append(i)
    
y = []

for i in n:
    y.append(get_mean(i, 0.34))
    
plt.plot(n, y)
plt.show()