from collections import deque
import grafo


def busca_em_profundidade(grafo, no_inicial, objetivo):

    stack = [(no_inicial, [no_inicial])]
    visited = set()

    while stack:
        no, caminho = stack.pop()
        if no == objetivo:
            return caminho
        if no not in visited:
            visited.add(no)
            for neighbor in grafo.neighbors(no):
                if neighbor not in visited:
                    stack.append((neighbor, caminho + [neighbor]))
    return "Caminho não encontrado"

#Executando 

if __name__ == "__main__":
    mapa_romenia = grafo.mapa_romenia()
    no_inicial = 'Arad'
    objetivo = 'Bucharest'
    caminho = busca_em_profundidade(mapa_romenia, no_inicial, objetivo)
    print("Caminho encontrado:", caminho)
