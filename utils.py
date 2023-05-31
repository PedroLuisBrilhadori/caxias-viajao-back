import numpy as np

def euclidian_distance(i, j, nodes):
    return np.sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2)


def read_file(file): 
      with open(file) as f:
        lines = f.readlines()

        coordenadas = []
        tempoDeServico = []
        deadline = []

        for i in range(len(lines)):
            data = list(filter(None, lines[i].split(' ')))
            if len(data) > 2 and len(data) < 5:
                coordenadas.append([int(data[0]), int(data[1])])
                tempoDeServico.append(int(data[2]))
                deadline.append(int(data[3].replace('\n', '')))

        return (coordenadas, tempoDeServico, deadline)
