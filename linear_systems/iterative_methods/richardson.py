import numpy as np
from math import cos, pi, log


# Modified Richardson iteration
def jacobi_eigenvalue(n, a, col):
    d = np.zeros(n)
    bw = np.zeros(n)
    zw = np.zeros(n)

    it_num = 0
    k = 1

    for i in range(n):
        d[i] = a[i, i]
        bw[i] = d[i]

    signum = np.sqrt(np.max(abs(d))) * (10 ** -k)

    while True:
        it_num += 1
        diagonal = 0
        flag = True

        for j in range(n):
            for i in range(j):
                if a[i, j] > signum:
                    flag = False
                diagonal += abs(a[i, j])

        diagonal = diagonal / (4 * n)

        if flag:
            if k < col:
                k += 1
                signum = np.sqrt(np.max(abs(d))) * (10 ** -k)
            else:
                break

        for p in range(n):
            for q in range(p + 1, n):
                gapq = 10 * abs(a[p, q])
                termp = gapq + abs(d[p])
                termq = gapq + abs(d[q])

                if 4 < it_num and termp == abs(d[p]) and termq == abs(d[q]):
                    a[p, q] = 0
                elif diagonal <= abs(a[p, q]):
                    h = d[q] - d[p]
                    term = abs(h) + gapq

                    if term == abs(h):
                        t = a[p, q] / h
                    else:
                        theta = 0.5 * h / a[p, q]
                        t = 1 / (abs(theta) + np.sqrt(1 + theta * theta))
                        if theta < 0:
                            t = - t

                    c = 1 / np.sqrt(1 + t * t)
                    s = t * c
                    tau = s / (1 + c)
                    h = t * a[p, q]

                    zw[p] -= h
                    zw[q] += h
                    d[p] -= h
                    d[q] += h

                    a[p, q] = 0

                    for j in range(p):
                        g = a[j, p]
                        h = a[j, q]
                        a[j, p] = g - s * (h + g * tau)
                        a[j, q] = h + s * (g - h * tau)

                    for j in range(p + 1, q):
                        g = a[p, j]
                        h = a[j, q]
                        a[p, j] = g - s * (h + g * tau)
                        a[j, q] = h + s * (g - h * tau)

                    for j in range(q + 1, n):
                        g = a[p, j]
                        h = a[q, j]
                        a[p, j] = g - s * (h + g * tau)
                        a[q, j] = h + s * (g - h * tau)

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


def solve_le(data):
    eps = 10 ** -5
    n = data.shape[0]
    x = np.zeros(n)
    matrix = data[:, :len(data[0]) - 1]
    matrix_c = matrix.copy()
    b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))

    eigenvalues = jacobi_eigenvalue(n, matrix_c, 10)
    print(eigenvalues)
    t_0 = 2 / (max(eigenvalues) + min(eigenvalues))
    eta = min(eigenvalues) / max(eigenvalues)
    iterations = int(log(2 / eps) / (2 * np.sqrt(abs(eta))))
    f_0 = (1 - eta) / (1 + eta)

    for i in range(1, iterations):
        v = cos(((2 * i - 1) * pi) / (2 * iterations))
        t = t_0 / (1 + v * f_0)
        x = x - t * (matrix.dot(x) - b)

    return x