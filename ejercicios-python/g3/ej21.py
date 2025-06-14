import numpy as np

M = np.array([
    [0.61, 0.29, 0.150],
    [0.32, 0.59, 0.063],
    [0.04, 0.12, 0.787]
])

# invertir la matriz
M_inv = np.linalg.inv(M)

# mostrar la matriz inversa: XYZ -> RGB
print("Matriz de conversión de XYZ a RGB (inversa):")
print(np.round(M_inv, 4))