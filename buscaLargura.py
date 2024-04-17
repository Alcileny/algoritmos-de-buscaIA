from collections import deque
import grafo


def busca_em_largura(grafo, no_inicial, objetivo):

    queue = deque([(no_inicial, [no_inicial])])
    visitados = set()

    while queue:
        no, caminho = queue.popleft()
        if no == objetivo:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for neighbor in grafo.neighbors(no):
                if neighbor not in visitados:
                    queue.append((neighbor, caminho + [neighbor]))
    return "Caminho não encontrado"


if __name__ == "__main__":  
    mapa_romenia = grafo.mapa_romenia()
    no_inicial = 'Arad'
    objetivo = 'Bucharest'
    caminho = busca_em_largura(mapa_romenia, no_inicial, objetivo)
    print("Caminho encontrado:", caminho)
    
