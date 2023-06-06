from utils.read_data import read_string

def variables(data): 
    coordenadas, tempoDeServico, deadline = read_string(data)

    n = len(coordenadas)

    M = sum(deadline) + 10

    return (n, coordenadas, tempoDeServico, deadline, M)
