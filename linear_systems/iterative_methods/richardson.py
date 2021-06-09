import numpy as np
from math import cos, pi


# Modified Richardson iteration
def jacobi_eigenvalue(n, a, it_max: int, P):
    count = 0
    d = np.zeros(n)
    bw = np.zeros(n)
    zw = np.zeros(n)
    k = 0

    for i in range(n):
        d[i] = a[i, i]
        bw[i] = d[i]

    it_num = 0

    while it_num < it_max:
        if (k < P):
            k += 1
        it_num += 1
        diagonal = 0

        max = np.sqrt(np.max(d))
        sigma = max * (10 ** -k)

        check = True
        for j in range(n):
            for i in range(j):
                if a[i, j] > sigma:
                    check = False

        if (check):
            break

        for p in range(n):
            for q in range(p + 1, n):
                gapq = 100 * abs(a[p, q])
                termp = gapq + abs(d[p])
                termq = gapq + abs(d[q])

                if 4 < it_num and termp == abs(d[p]) and termq == abs(d[q]):
                    a[p, q] = 0
                elif diagonal <= abs(a[p, q]):
                    h = d[q] - d[p]

                    if abs(h) + gapq == abs(h):
                        t = a[p, q] / h
                    else:
                        theta = 0.5 * h / a[p, q]
                        t = 1 / (abs(theta) + np.sqrt(1.0 + theta * theta))
                        if theta < 0:
                            t = - t

                    c = 1 / np.sqrt(1 + t ** 2)
                    s = t * c
                    tau = s / (1 + c)
                    h = t * a[p, q]

                    zw[p] -= h
                    zw[q] += + h
                    d[p] -= - h
                    d[q] += + h
                    a[p, q] = 0

                    for j in range(p):
                        a[j, p] = a[j, p] - s * (a[j, q] + a[j, p] * tau)
                        a[j, q] = a[j, q] + s * (a[j, p] - a[j, q] * tau)

                    for j in range(p + 1, q):
                        a[p, j] = a[p, j] - s * (a[j, q] + a[p, j] * tau)
                        a[j, q] = a[j, q] + s * (a[p, j] - a[j, q] * tau)

                    for j in range(q + 1, n):
                        a[p, j] = a[p, j] - s * (a[q, j] + a[p, j] * tau)
                        a[q, j] = a[q, j] + s * (a[p, j] - a[q, j] * tau)

        for i in range(n):
            bw[i] += zw[i]
            d[i] = bw[i]
            zw[i] = 0

    for k in range(n - 1):
        m = k

        for l in range(k + 1, n):
            if d[l] < d[m]:
                m = l

        if k != m:
            t = d[m]
            d[m] = d[k]
            d[k] = t

    print(it_num)
    return d


def solve_le(data, iterations: int):
    n = data.shape[0]
    x = np.zeros(n)
    matrix = data[:, :len(data[0]) - 1]
    matrix_c = matrix.copy()
    b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))

    eigenvalues = jacobi_eigenvalue(n, matrix_c, 1000, 100)
    t_0 = 2 / (max(eigenvalues) + min(eigenvalues))
    eta = min(eigenvalues) / max(eigenvalues)
    f_0 = (1 - eta) / (1 + eta)

    for i in range(1, iterations):
        v = cos(((2 * i - 1) * pi) / (2 * iterations))
        t = t_0 / (1 + v * f_0)
        x = x - t * (matrix.dot(x) - b)

    return x
