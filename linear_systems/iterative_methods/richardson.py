import numpy as np
from math import cos, pi


# Modified Richardson iteration
def solve_le(data, iterations: int):
    n = data.shape[0]
    x = np.zeros(n)
    matrix = data[:, :len(data[0]) - 1]
    b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))
    eigenvalues, vec = np.linalg.eig(matrix)
    t_0 = 2 / (max(eigenvalues) + min(eigenvalues))
    eta = min(eigenvalues) / max(eigenvalues)
    f_0 = (1 - eta) / (1 + eta)

    for i in range(1, iterations):
        v = cos(((2 * i - 1) * pi) / (2 * iterations))
        t = t_0 / (1 + v * f_0)
        x = x - t * (matrix.dot(x) - b)

    return x
