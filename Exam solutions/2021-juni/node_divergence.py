import numpy as np


def node_divergence(A):
    assert isinstance(A, np.ndarray)
    nodes = []
    for row in A:
        if not nodes.__contains__(row[0]):
            nodes.append(row[0])
        if not nodes.__contains__(row[1]):
            nodes.append(row[1])
    nodes.sort()
    D = np.zeros(shape=(len(nodes),2))
    for index, node in enumerate(nodes, 0):
        orig = [row for row in A if row[0] == node]
        dest = [row for row in A if row[1] == node]
        sumOrig = sum([lst[2] for lst in orig])
        sumDest = sum([lst[2] for lst in dest])
        d = sumOrig - sumDest
        D[index][0] = node
        D[index][1] = d
    return D
