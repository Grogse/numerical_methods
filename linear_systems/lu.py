import numpy as np


# LU - Decomposition
def matrix_to_lu(matrix):
    n = matrix.shape[0]
    matrix_lu = np.matrix(np.zeros([n, n]))

    for k in range(n):
        for j in range(k, n):
            matrix_lu[k, j] = matrix[k, j] - matrix_lu[k, :k] * matrix_lu[:k, j]
        for i in range(k + 1, n):
            matrix_lu[i, k] = (matrix[i, k] - matrix_lu[i, :k] * matrix_lu[:k, k]) / matrix_lu[k, k]

    return matrix_lu


def create_l(matrix_lu):
    l = matrix_lu.copy()

    for i in range(l.shape[0]):
        l[i, i] = 1
        l[i, i + 1:] = 0

    return np.matrix(l)


def create_u(matrix_lu):
    u = matrix_lu.copy()

    for i in range(1, u.shape[0]):
        u[i, :i] = 0

    return np.matrix(u)


def matrix_det(matrix):
    return round(np.linalg.det(matrix))


def solve_slay(data):
    matrix = data[:, :len(data[0]) - 1]
    b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))

    matrix_lu = matrix_to_lu(matrix)
    n = matrix_lu.shape[0]
    y = np.matrix(np.zeros([matrix_lu.shape[0], 1]))
    x = np.matrix(np.zeros([matrix_lu.shape[0], 1]))

    for i in range(n):
        y[i] = b[i] - matrix_lu[i, :i] * y[:i]

    for i in range(1, n + 1):
        x[-i] = (y[-i] - matrix_lu[-i, -i:] * x[-i:]) / matrix_lu[-i, -i]

    res = np.squeeze(np.asarray(x))

    for i in range(n):
        res[i] = round(res[i], 7)

    return res
