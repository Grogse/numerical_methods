import numpy as np
from linear_systems.iterative_methods import richardson

data = np.loadtxt('input.txt')
matrix_a = data[:, :len(data[0]) - 1]
vector_b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))

print(richardson.solve_le(data, 10))
