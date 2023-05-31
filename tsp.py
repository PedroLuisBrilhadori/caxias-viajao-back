from pymprog import iprod, begin, minimize, solve, end, var
from models import TspRoute
from utils import euclidian_distance, read_file

def get_tsp_routes(file): 
    tspRoutes = []

    begin("caixeiro") # Início do modelo

    n, x, z, phi, coordenadas, tempoDeServico, deadline, M = variables(file)

    # Modelo / Função Objetivo
    minimize(sum(z[j] for j in range(1, n-1))) 

    x = restricoes(n, x)

    x, z, phi = exclude_sub_routes(n, x, z, phi, M, coordenadas, tempoDeServico, deadline)

    solve()
    end()
    
    tspRoutes = get_routes(n, x, coordenadas)

    return tspRoutes

def variables(file): 
    coordenadas, tempoDeServico, deadline = read_file(file)

    # Variáveis de decisão
    n = len(coordenadas)
    
    prod = iprod(range(n), range(n))

    x = var("x", prod, bool)
    # Quantifica o atraso em cada nó
    z = var("z", n) 
    
    # Variável que representa o instante de início do tempo de serviço, realizando o acumulo de tempo decorrido
    phi = var("phi", n) 

    M = sum(deadline) + 10



    return (n, x, z, phi, coordenadas, tempoDeServico, deadline, M)


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
    expand = 3

    for i in range(n-1):
        for j in range(1, n):
            if round(x[i,j].primal) == 1:
                target = j

                if j == (n - 1):
                    target = 0

                route = TspRoute(i, target, coordenadas[i][0] * expand, coordenadas[i][1] * expand).__dict__
                routes.append(route)

    return routes
