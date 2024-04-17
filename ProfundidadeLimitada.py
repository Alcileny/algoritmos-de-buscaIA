from collections import deque
import grafo


def busca_em_profundidade_limitada(grafo, no_inicial, objetivo, limite):

    stack = [(no_inicial, [no_inicial])]
    visited = set()

    while stack:
        no, caminho = stack.pop()
        if no == objetivo:
            return caminho
        if len(caminho) < limite:
            
            if no not in visited:
                visited.add(no)
                for neighbor in grafo.neighbors(no):
                    if neighbor not in visited:
                        stack.append((neighbor, caminho + [neighbor]))
    return "Caminho não encontrado"



if __name__ == "__main__":
    mapa_romenia = grafo.mapa_romenia()
    no_inicial = 'Arad'
    objetivo = 'Bucharest'
    limite_profundidade = 4
    caminho = busca_em_profundidade_limitada(mapa_romenia, no_inicial, objetivo, limite_profundidade)
    print("Caminho encontrado:", caminho)