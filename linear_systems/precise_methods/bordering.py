import numpy as np


# Bordering method
def inv_matrix(matrix):
    n = matrix.shape[0]

    if n == 1:
        return 1 / matrix[0, 0]

    inv_mat = matrix.copy()
    inv_mat[0, 0] = 1 / inv_mat[0, 0]

    for k in range(1, n):
        mat_k = inv_mat[:k, :k]
        u_k = np.matrix(np.zeros([k, 1]))
        for i in range(k):
            u_k[i] = inv_mat[i, k]
        v_k = inv_mat[k, :k]
        m_kk = inv_mat[k, k]

        y_k = v_k.dot(mat_k)
        x_k = mat_k.dot(u_k)
        z_k = v_k * x_k
        m_k = np.squeeze(np.asarray(m_kk - z_k))

        inv_mat[k, k] = 1 / m_k
        inv_mat[k, :k] = -(1 / m_k) * y_k
        inv_mat[:k, k] = -(1 / m_k) * np.squeeze(x_k)
        inv_mat[:k, :k] = mat_k + ((1 / m_k) * x_k * y_k)

    return inv_mat


def solve_le(data):
    matrix = data[:, :len(data[0]) - 1]
    b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))

    inv_mat = inv_matrix(matrix)

    return np.round(inv_mat.dot(b), 7)
