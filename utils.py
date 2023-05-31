import numpy as np

def euclidian_distance(i, j, nodes):
    return np.sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2)