import numpy as np

A = np.array([
    [1/6, 1/2, 1/3],
    [1/2, 1/4, 1/4],
    [1/3, 1/4, 5/12]
])

# potencias sucesivas
for k in [1, 5, 10, 100]:
    Ak = np.linalg.matrix_power(A, k)
    print(f"A^{k}:")
    print(np.round(Ak, 4))
    print()

'''
    Se empiezan a parecer cada vez más los números
'''
