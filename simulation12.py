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
    temp = sum(l)/len(l)
    return temp

n = []
for i in range(50, 1201, 50):
    n.append(i)
    
y = []

for i in n:
    y.append(get_mean(i, 1/i))
    
plt.plot(n, y)
plt.show()
y2 = []
for i in range(len(y)):
    s = 0
    for j in range(i + 1):
        s += y[j]
    s = s / (i + 1)
    y2.append(s)
        
    
    
plt.plot(n, y2)
plt.show()