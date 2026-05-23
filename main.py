from grafo import grafo_A, grafo_B
from mis import ejecutar as mis
from minimax import ejecutar as minimax

print("Escenario A")
mis(grafo_A(), "A (10 nodos)")
minimax(grafo_A(), "N0", "N9", "A (10 nodos)")

print("Escenario B")
mis(grafo_B(), "B (denso)")
minimax(grafo_B(), "N0", "N5", "B (denso)")
