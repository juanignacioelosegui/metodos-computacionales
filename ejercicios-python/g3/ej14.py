import numpy as np
from itertools import product

M = np.array([
    [1, 0, -1, 0],
    [0, 1,  0, 0],
    [-1, 0, 1, 0],
    [0, 0,  0, 1]
])

# generar todos los vectores no nulos de {0, 1}^4
vectors = [np.array(x) for x in product([0, 1], repeat=4) if any(x)]

# buscar cuáles son detectados por M (x^T M x == 0)
print("Probando vectores binarios de R^4 con xᵀ M x:")
for x in vectors:
    value = x @ M @ x  # xᵀ M x
    if value == 0:
        print(f"Vector {x} detectado. xᵀ M x = 0")
    else:
        print(f"Vector {x} no detectado. xᵀ M x = {value}")