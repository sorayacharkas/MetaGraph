import matplotlib.pyplot as plt
from numpy import *
import networkx as nx
def diameter_mean(n, p):
    l = []
    for _ in range(100):
        g = nx.gnp_random_graph(n, p)
        try:
            l.append(nx.diameter(g))
        except:
            continue
    return sum(l)/len(l)

x = []
y = []
for i in range(10, 201, 10):
    x.append(i)
    y.append(diameter_mean(i, 0.34))

plt.plot(x, y)
plt.show()