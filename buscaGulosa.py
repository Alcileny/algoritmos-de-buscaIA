import heapq
import networkx as nx
from grafo import mapa_romenia

def busca_gulosa(mapa, estado_inicial, estado_meta):
    fila_prioridade = []
    visitados = set()
    caminho = []

    heapq.heappush(fila_prioridade, (mapa.nodes[estado_inicial]['heuristica'], estado_inicial))

    while fila_prioridade:
        heuristica, proximo_estado = heapq.heappop(fila_prioridade)

        if proximo_estado == estado_meta:
            caminho.append(proximo_estado)
            break

        if proximo_estado not in visitados:
            visitados.add(proximo_estado)
            caminho.append(proximo_estado)

            for vizinho in mapa.neighbors(proximo_estado):
                if vizinho not in visitados:
                    heuristica_vizinho = mapa.nodes[vizinho]['heuristica']
                    heapq.heappush(fila_prioridade, (heuristica_vizinho, vizinho))

    if caminho[-1] != estado_meta:
        print("Caminho não encontrado.")
        return None

    return caminho

if __name__ == "__main__":
    mapa = mapa_romenia()
    estado_inicial = 'Arad'
    estado_meta = 'Bucharest'

    caminho = busca_gulosa(mapa, estado_inicial, estado_meta)

    if caminho:
        print("Caminho encontrado:", caminho)
    else:
        print("Caminho não encontrado.")
