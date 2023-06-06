from utils.math import euclidian_distance

def constraints(n, x): 
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