from numpy import sqrt

def euclidian_distance(i, j, nodes):
    return sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2)

