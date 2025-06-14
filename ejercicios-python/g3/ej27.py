import numpy as np

def block_matrix_multiply(A, B, block_size):
    assert A.shape == B.shape, "Las matrices deben ser cuadradas y del mismo tamaño"
    N = A.shape[0]
    C = np.zeros((N, N))

    # recorrer por bloques
    for i in range(0, N, block_size):
        for j in range(0, N, block_size):
            for k in range(0, N, block_size):
                # Extraemos los subbloques
                A_block = A[i:i+block_size, k:k+block_size]
                B_block = B[k:k+block_size, j:j+block_size]

                # Tamaño de bloque real (puede ser menor en los bordes)
                bi = A_block.shape[0]
                bj = B_block.shape[1]

                # Aseguramos compatibilidad en el cálculo
                C_block = np.dot(A_block, B_block)
                C[i:i+bi, j:j+bj] += C_block

    return C

A = np.random.randint(0, 10, (6, 6))
B = np.random.randint(0, 10, (6, 6))

C = block_matrix_multiply(A, B, block_size=2)

print("Matriz A:\n")
print(A, "\n")
print("Matriz B:\n")
print(B, "\n")
print("¿Resultado correcto?:", np.allclose(C, A @ B), "\n")
print("Matriz C:\n")
print(C, "\n")