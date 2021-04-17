import numpy as np
import numpy.linalg as lin
import math


# QR - Decomposition
def proj(a, b):
    return (np.dot(a, b) / np.dot(b, b)) * b


def qr_decomposition(matrix):
    n = matrix.shape[0]
    q = matrix.copy()
    q_1 = np.zeros(n)

    for i in range(n):
        for j in range(i):
            q_1 += proj(matrix[:, i], q[:, j])
        q[:, i] = matrix[:, i] - q_1
        q[:, i] = q[:, i] / math.sqrt(np.dot(q[:, i], q[:, i]))
        q_1 = np.zeros(n)

    return q


def create_r(matrix):
    return lin.inv(qr_decomposition(matrix)).dot(matrix)


def solve_le(data):
    matrix = data[:, :len(data[0]) - 1]
    b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))

    q = qr_decomposition(matrix)
    r = create_r(matrix)
    x = np.round((lin.inv(r).dot(np.transpose(q))).dot(b), 7)

    return x
