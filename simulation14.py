import matplotlib.pyplot as plt
from numpy import * 
import numpy as np
import networkx as nx
def connected_no_friends(n, p):
    c = [] # true, false for connected
    l = [] # num no friends
    for _ in range(100):
        g = nx.gnp_random_graph(n, p)
        c.append(nx.is_connected(g))
        num = 0
        for i in range(n):
            if len(g.adj[i]) == 0:
                num += 1
        l.append(num)
    return (sum(c)/len(c), sum(l)/(len(l)*n))


def p(n):
    return (4*np.log(n))/(n)

x = []
y1 = []
y2 = []
for i in range(10, 151, 10):
    x.append(i)
    temp = connected_no_friends(i, p(i))
    y1.append(temp[0])
    y2.append(temp[1])

plt.plot(x, y1)
plt.show()


