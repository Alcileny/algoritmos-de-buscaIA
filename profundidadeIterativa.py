import grafo

def busca_em_profundidade_iterativa(grafo, no_inicial, objetivo):
    limite_profundidade = 0
    while True:
        resultado = busca_em_profundidade_limitada(grafo, no_inicial, objetivo, limite_profundidade)
        if resultado != "Caminho não encontrado":
            return resultado
        limite_profundidade += 1

def busca_em_profundidade_limitada(grafo, no_inicial, objetivo, limite_profundidade):
    stack = [(no_inicial, [no_inicial])]
    visited = set()

    while stack:
        no, caminho = stack.pop()
        if no == objetivo:
            return caminho
        if len(caminho) < limite_profundidade:
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
    caminho = busca_em_profundidade_iterativa(mapa_romenia, no_inicial, objetivo)
    print("Caminho encontrado:", caminho)