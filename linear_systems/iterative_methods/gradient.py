import numpy as np


# Naive Line Search for Gradient Descent
def solfe_le(data):
    n = data.shape[0]
    eps = 10 ** -3
    x = np.zeros(n)
    a = data[:, :len(data[0]) - 1]
    b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))

    while True:
        f = a.dot(x) - b
        if max(abs(f)) < eps:
            return x

        r = b - a.dot(x)
        lambd = (r.dot(r)) / (r.dot(a.dot(r)))
        x = x - f.dot(lambd)
