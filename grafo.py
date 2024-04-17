import matplotlib.pyplot as plot
import networkx as nx

def mapa_romenia():
    mapa = nx.Graph()

    mapa.add_nodes_from([
        ('Arad',{'heuristica':366}),
        ('Zerind',{'heuristica':374}),
        ('Oradea',{'heuristica':380}),
        ('Sibiu',{'heuristica':253 }),
        ('Timisoara',{'heuristica':329}),
        ('Lugoj',{'heuristica':244}),
        ('Mehadia',{'heuristica':241}),
        ('Drobeta',{'heuristica':242}),
        ('Craiova',{'heuristica':160}),
        ('Rimnicu',{'heuristica':193}),
        ('Fagaras',{'heuristica':176}),
        ('Pitesti',{'heuristica':100}),
        ('Bucharest',{'heuristica':0}),
        ('Giurgiu',{'heuristica':77}),
        ('Urziceni',{'heuristica':80}),
        ('Hirsova',{'heuristica':151}),
        ('Eforie',{'heuristica':161}),
        ('Vaslui',{'heuristica':199}),
        ('Iasi',{'heuristica':226}),
        ('Neamt',{'heuristica':234})
        ])

    mapa.add_edges_from([
        ('Arad' , 'Zerind', {'custo': 75}),
        ('Arad' , 'Timisoara', {'custo': 118}),
        ('Arad' , 'Sibiu', {'custo': 140}),
        ('Zerind','Oradea',{'custo': 71}),
        ('Sibiu','Rimnicu',{'custo': 80}),
        ('Sibiu','Fagaras',{'custo': 99}),
        ('Timisoara','Lugoj', {'custo': 111}),
        ('Oradea','Sibiu',{'custo':151}),
        ('Lugoj','Mehadia',{'custo':70}),
        ('Mehadia','Drobeta',{'custo':75}),
        ('Drobeta','Craiova',{'custo':120}),
        ('Rimnicu','Craiova',{'custo':146}),
        ('Pitesti','Craiova',{'custo':138}),
        ('Rimnicu','Pitesti',{'custo':97}),
        ('Fagaras','Bucharest',{'custo':211}),
        ('Pitesti','Bucharest',{'custo':101}),
        ('Bucharest','Giurgiu',{'custo':90}),
        ('Bucharest','Urziceni',{'custo':85}),
        ('Urziceni','Hirsova',{'custo':98}),
        ('Urziceni','Vaslui',{'custo':142}),
        ('Hirsova','Eforie',{'custo':86}),
        ('Vaslui','Iasi',{'custo':92}),
        ('Iasi','Neamt',{'custo':87})
    ])

    return mapa





