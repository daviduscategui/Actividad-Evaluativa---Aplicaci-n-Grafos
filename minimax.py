import networkx as nx
import heapq
import time
from grafo import grafo_A, grafo_B

def aprox_minimax(G, src, dst):
    bot = {n: float("inf") for n in G.nodes()}
    bot[src] = 0
    prev = {n: None for n in G.nodes()}
    heap = [(0, src)]
    vis = set()
    while heap:
        cb, u = heapq.heappop(heap)
        if u in vis:
            continue
        vis.add(u)
        if u == dst:
            break
        for v in G.successors(u):
            w = G[u][v]["weight"]
            ncb = max(cb, w)
            if ncb < bot[v]:
                bot[v] = ncb
                prev[v] = u
                heapq.heappush(heap, (ncb, v))
    ruta = []
    n = dst
    while n is not None:
        ruta.append(n)
        n = prev[n]
    ruta.reverse()
    if ruta[0] != src:
        return float("inf"), []
    return bot[dst], ruta

def ejecutar(G, src, dst, nombre):
    t0 = time.perf_counter()
    cb, ruta = aprox_minimax(G, src, dst)
    t1 = time.perf_counter()
    print(f"\n[MINIMAX] {nombre}")
    print(f"  Ruta   : {' -> '.join(ruta)}")
    print(f"  Cuello : {cb}")
    print(f"  Tiempo : {(t1-t0)*1000:.4f} ms")

if __name__ == "__main__":
    ejecutar(grafo_A(), "N0", "N9", "Escenario A (10 nodos)")
    ejecutar(grafo_B(), "N0", "N5", "Escenario B (denso)")
