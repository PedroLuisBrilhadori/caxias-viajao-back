import numpy as np
import json

def euclidian_distance(i, j, nodes):
    return np.sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2)

def writeCache(file, routes): 
    with open(file, 'w') as file: 
        file.write(json.dumps(routes))
        file.close()

def read_string(string: str): 
    lines = string.split('\n')

    coordenadas = []
    tempoDeServico = [0]
    deadline = [0]
    first = []
    
    for i in range(len(lines)):
        data = list(filter(None, lines[i].split(' ')))
        if len(data) > 2 and len(data) < 5:
            coordenadas.append([int(data[0]), int(data[1])])
            tempoDeServico.append(int(data[2]))
            deadline.append(int(data[3].replace('\n', '')))
        
        if len(data) == 2: 
            first = [int(data[0]), int(data[1])]
    coordenadas.insert(0, first)
    coordenadas.append(first)
    return (coordenadas, tempoDeServico, deadline)        