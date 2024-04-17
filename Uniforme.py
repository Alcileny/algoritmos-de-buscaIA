import heapq 
import grafo


def busca_uniforme(grafo, no_inicial, objetivo):

    queue = [(0, no_inicial, [no_inicial])]  
    visitados = set()

    while queue:
        custo, no, caminho = heapq.heappop(queue)
        if no == objetivo:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for neighbor in grafo.neighbors(no):
                if neighbor not in visitados:
                    custo_vizinho = grafo[no][neighbor]['custo']
                    heapq.heappush(queue, (custo + custo_vizinho, neighbor, caminho + [neighbor]))  #Verifica a prioridade de custo de um no e organiza a fila
    return "Caminho não encontrado"



if __name__ == "__main__":
    mapa_romenia = grafo.mapa_romenia()
    no_inicial = 'Arad'
    objetivo = 'Bucharest'
    caminho = busca_uniforme(mapa_romenia, no_inicial, objetivo)
    print("Caminho encontrado:", caminho)