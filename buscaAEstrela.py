import networkx as nx 
import heapq
from grafo import mapa_romenia

def busca_a_star(mapa, inicio, objetivo):
    
    if inicio not in mapa.nodes or objetivo not in mapa.nodes:
        raise ValueError("Nós de início ou objetivo não estão no grafo.")

    
    def heuristica(nodo):
        return mapa.nodes[nodo]['heuristica']

    
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0 + heuristica(inicio), 0, inicio, []))  

    visitados = set()

    while fila_prioridade:
        _, custo_g, atual, caminho = heapq.heappop(fila_prioridade)

        if atual in visitados:
            continue

        if atual == objetivo:
            return caminho + [atual]

        visitados.add(atual)

        for vizinho in mapa.neighbors(atual):
            if vizinho not in visitados:
                novo_custo_g = custo_g + mapa.edges[atual, vizinho]['custo']
                novo_caminho = caminho + [atual]
                heapq.heappush(fila_prioridade, (novo_custo_g + heuristica(vizinho), novo_custo_g, vizinho, novo_caminho))

    return None

if __name__ == "__main__":
    
    mapa = mapa_romenia()

    inicio = 'Arad'
    objetivo = 'Bucharest'

    caminho = busca_a_star(mapa, inicio, objetivo)

    if caminho:
        print("Caminho encontrado:", caminho)
        custo_total = sum(mapa.edges[caminho[i], caminho[i+1]]['custo'] for i in range(len(caminho) - 1))
        print("Custo total do caminho:", custo_total)
    else:
        print("Caminho não encontrado.")
