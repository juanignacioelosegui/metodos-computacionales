import numpy as np

# Definimos la matriz S
S = np.array([
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
], dtype=int)

# Calculamos S^k * 2 para k = 2, 3, ..., 6
for k in range(2, 7):
    Sk = np.linalg.matrix_power(S, k)
    result = 2 * Sk
    print(f"S^{k} * 2:")
    print(result)
    print()