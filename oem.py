import numpy as np


# Optimum exclusion method
def solve_slay(matrix):
    n = matrix.shape[0]
    x = np.zeros((matrix.shape[0],))
    a = matrix[0][0]

    for i in range(matrix.shape[1]):
        matrix[0][i] = matrix[0][i] / a

    for k in range(1, n):
        tmp = matrix.copy()
        for i in range(matrix.shape[1]):
            a_1 = a_2 = 0

            for j in range(k):
                a_1 += tmp[j][i] * tmp[k][j]
            for j in range(k):
                a_2 += tmp[j][k] * tmp[k][j]

            matrix[k][i] = (tmp[k][i] - a_1) / (tmp[k][k] - a_2)

        for q in range(k):
            for i in range(matrix.shape[1]):
                matrix[q][i] = tmp[q][i] - (matrix[k][i] * tmp[q][k])

    for i in range(n):
        x[i] = round(matrix[i][matrix.shape[1] - 1], 7)

    return x
