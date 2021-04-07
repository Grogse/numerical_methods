import numpy as np


# Optimum exclusion method
def solve_slay(data):
    mat = data.copy()
    n = mat.shape[0]
    x = np.zeros((mat.shape[0],))
    a = mat[0][0]

    for i in range(mat.shape[1]):
        mat[0][i] = mat[0][i] / a

    for k in range(1, n):
        tmp = mat.copy()
        for i in range(mat.shape[1]):
            a_1 = a_2 = 0

            for j in range(k):
                a_1 += tmp[j][i] * tmp[k][j]
            for j in range(k):
                a_2 += tmp[j][k] * tmp[k][j]

            mat[k][i] = (tmp[k][i] - a_1) / (tmp[k][k] - a_2)

        for q in range(k):
            for i in range(mat.shape[1]):
                mat[q][i] = tmp[q][i] - (mat[k][i] * tmp[q][k])

    for i in range(n):
        x[i] = round(mat[i][mat.shape[1] - 1], 7)

    return x
