import networkx as nx
import time
from grafo import grafo_A, grafo_B

def aprox_mis(G):
    Gu = G.to_undirected()
    cands = set(Gu.nodes())
    mis = []
    while cands:
        sg = Gu.subgraph(cands)
        n = min(sg.nodes(), key=lambda x: sg.degree(x))
        mis.append(n)
        cands -= {n} | set(Gu.neighbors(n))
    return mis

def verificar(G, mis):
    Gu = G.to_undirected()
    for i in range(len(mis)):
        for j in range(i+1, len(mis)):
            if Gu.has_edge(mis[i], mis[j]):
                return False
    return True

def ejecutar(G, nombre):
    t0 = time.perf_counter()
    res = aprox_mis(G)
    t1 = time.perf_counter()
    valido = verificar(G, res)
    print(f"\n[MIS] {nombre}")
    print(f"  Conjunto : {res}")
    print(f"  Tamaño   : {len(res)}/{G.number_of_nodes()}")
    print(f"  Válido   : {valido}")
    print(f"  Tiempo   : {(t1-t0)*1000:.4f} ms")

if __name__ == "__main__":
    ejecutar(grafo_A(), "Escenario A (10 nodos)")
    ejecutar(grafo_B(), "Escenario B (denso)")
