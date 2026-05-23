import networkx as nx
import random

def grafo_A():
    G = nx.DiGraph()
    nds = [f"N{i}" for i in range(10)]
    G.add_nodes_from(nds)
    ars = [
        ("N0","N1",4),("N0","N2",7),("N1","N3",2),("N1","N4",5),
        ("N2","N3",1),("N2","N5",8),("N3","N6",3),("N4","N6",6),
        ("N4","N7",4),("N5","N7",2),("N5","N8",9),("N6","N9",5),
        ("N7","N9",3),("N8","N9",1),("N3","N8",7),("N1","N5",6),
        ("N0","N4",3),("N6","N8",2),
    ]
    for u,v,w in ars:
        G.add_edge(u,v,weight=w)
    return G

def grafo_B():
    random.seed(42)
    G = nx.DiGraph()
    nds = [f"N{i}" for i in range(6)]
    G.add_nodes_from(nds)
    for i in range(6):
        for j in range(6):
            if i != j:
                G.add_edge(nds[i], nds[j], weight=random.randint(1,20))
    return G
