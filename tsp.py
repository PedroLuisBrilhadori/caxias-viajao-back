from pymprog import var, iprod, begin, minimize, solve, end
import numpy as np
from models import TspRoute

def euclidian_distance(i, j, nodes):
    return np.sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2)

def restricoes(n, x): 
    # Restrições
    for j in range(1, n):
        sum(x[i, j] for i in range(n-1) if i != j) == 1

    for i in range(n-1):
        sum(x[i, j] for j in range(1, n) if i != j) == 1
    return x

def exclude_sub_routes(n, x, z, phi, M, coordenadas, tempoDeServico, deadline): 
    # Eliminação de sub-rotas
    for i in range(n-1):
        for j in range(1, n):
            phi[j] >= phi[i] + (M * x[i, j]) - M + (euclidian_distance(i, j, coordenadas) + tempoDeServico[i])

    for j in range(1, n-1):
        z[j] >= phi[j] - deadline[j]

    return (x, z, phi)

def get_routes(n, x, coordenadas): 
    routes = []

    for i in range(n-1):
        for j in range(1, n):
            if round(x[i,j].primal) == 1:
                target = j

                if j == (n - 1):
                    target = 0

                route = TspRoute(i, target, coordenadas[i][0], coordenadas[i][1])
                routes.append(route)

    return routes


def get_tsp_routes(): 
    tspRoutes = []

    begin("caixeiro") # Início do modelo

    #Variáveis de decisão
    n = len(coordenadas)
    
    prod = iprod(range(n), range(n))
    x = var("x", prod, bool)
    # Quantifica o atraso em cada nó
    z = var("z", n) 
    
    # Variável que representa o instante de início do tempo de serviço, realizando o acumulo de tempo decorrido
    phi = var("phi", n) 

    # Dados de entrada
    coordenadas = [
        [27, 45],
        [5, 96],
        [4, 87],
        [67, 5],
        [77, 100],
        [96, 24],
        [78, 68],
        [91, 64],
        [15, 26],
        [27, 45]
    ]

    tempoDeServico = [0, 9, 7, 8, 20 ,11, 17, 6, 7]

    deadline = [0, 430, 17, 449, 490, 428, 535, 28, 419]

    M = sum(deadline) + 10

    # Modelo / Função Objetivo
    minimize(sum(z[j] for j in range(1, n-1))) 

    x = restricoes(n, x)

    x, z, phi = exclude_sub_routes(n, x, z, phi, M, coordenadas, tempoDeServico, deadline)

    solve()
    end()
    
    tspRoutes = get_routes(n, x)

    return tspRoutes