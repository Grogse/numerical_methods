import numpy as np
import cmath


# Square root method
def matrix_to_s(matrix):
    s_1 = s_2 = 0
    n = matrix.shape[0]
    matrix_s = np.matrix(np.zeros([n, n], dtype=complex))
    matrix_s[0, 0] = cmath.sqrt(matrix[0, 0])

    for i in range(1, n):
        matrix_s[0, i] = matrix[0, i] / matrix_s[0, 0]

    for i in range(1, n):
        for k in range(i):
            s_1 += matrix_s[k, i] ** 2
        matrix_s[i, i] = cmath.sqrt(matrix[i, i] - s_1)

        for t in range(i + 1, n):
            for k in range(i):
                s_2 += matrix_s[k, i] * matrix_s[k, t]

            matrix_s[i, t] = (matrix[i, t] - s_2) / matrix_s[i, i]
            s_2 = 0

        s_1 = 0

    return matrix_s

def solve_slay(data):
    matrix = data[:, :len(data[0]) - 1]
    b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))

    n = matrix.shape[0]
    matrix_s = matrix_to_s(matrix)
    y = np.matrix(np.zeros([matrix_s.shape[0], 1], dtype=complex))
    x = np.matrix(np.zeros([matrix_s.shape[0], 1], dtype=complex))

    y[0] = b[0] / matrix_s[0, 0]
    s_1 = 0

    for i in range(1, n):
        for j in range(i):
            s_1 += matrix_s[j, i] * y[j]
        y[i] = (b[i] - s_1) / matrix_s[i, i]
        s_1 = 0

    x[n - 1] = y[n - 1] / matrix_s[n - 1, n - 1]
    s_1 = 0

    for i in range(2, n + 1):
        for j in range(n - i, n):
            s_1 += matrix_s[-i, j] * x[j]
        x[-i] = (y[-i] - s_1) / matrix_s[-i, -i]
        s_1 = 0

    res = np.zeros(n)

    for i in range(n):
        res[i] = x[i].real
        res[i] = round(res[i], 7)

    return res
