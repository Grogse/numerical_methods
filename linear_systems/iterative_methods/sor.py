import numpy as np

# Successive over-relaxation
def solve_le(data):
    n = data.shape[0]
    eps = 10 ** -3
    x = np.zeros(n)
    d = np.zeros(n)
    mat_c = data.copy()

    for i in range(n):
        for j in range(n + 1):
            mat_c[i, j] = -data[i, j] / data[i, i]
            if i == 0 and j < n:
                d[i] += mat_c[i, j] * x[j]
            if j == n:
                mat_c[i, j] *= -1
                d[i] += mat_c[i, j]

    while True:
        for k in range(n):
            if max(abs(d)) < eps:
                return x
            tmp = max(abs(d))
            for z in range(n):
                if abs(d[z]) == tmp:
                    x[z] += d[z]
            for i in range(n):
                d[i] = 0
                for j in range(n + 1):
                    if j < n:
                        d[i] += mat_c[i, j] * x[j]
                    if j == n:
                        d[i] += mat_c[i, j]
