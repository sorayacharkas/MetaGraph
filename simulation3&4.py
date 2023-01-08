import matplotlib.pyplot as plt
from numpy import *
import networkx as nx
n = 2000
p = 0.3

t = []
r = []
for _ in range(3):
    g = nx.gnp_random_graph(n, p)
    t_temp = 0
    r_temp = 0
    #creating every possible triangle
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n): #to check if they are T or R
                if i in g.adj[j] and i in g.adj[k] and k in g.adj[j]:
                    t_temp += 1
                elif i not in g.adj[j] and i in g.adj[k] and k in g.adj[j]:
                    r_temp += 1
                elif i in g.adj[j] and i not in g.adj[k] and k in g.adj[j]:
                    r_temp += 1
                elif i in g.adj[j] and i in g.adj[k] and k not in g.adj[j]:
                    r_temp += 1
            
    
    t.append(t_temp)
    r.append(r_temp)
