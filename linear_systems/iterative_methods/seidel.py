import numpy as np


# Seidel method
def solve_le(data):
    n = data.shape[0]
    eps = 10 ** -7
    x = np.zeros(n)
    x_0 = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))
    x_new = x_0.copy()
    mat_c = data.copy()

    for i in range(n):
        for j in range(n + 1):
            mat_c[i, j] = -data[i, j] / data[i, i]
            if j == n:
                mat_c[i, j] *= -1

    while max(abs(x - x_new) > eps):
        x_0 = x.copy()
        x_new = x.copy()
        x = np.zeros(n)
        for i in range(n):
            for j in range(n + 1):
                if j != n:
                    x[i] += mat_c[i, j] * x_0[j]
                else:
                    x[i] += mat_c[i, j]

            x[i] -= mat_c[i, i] * x_0[i]
            x_0[i] = x[i]

    return np.round(x, 10)
