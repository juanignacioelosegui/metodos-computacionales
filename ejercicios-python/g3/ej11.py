import numpy as np

# give me your seed bro
np.random.seed(42)

# cantidad de pruebas
n_tests = 5
size = 4

def test_identity_1():
    print("Testeando identidad (A + I)(A - I) = A^2 - I:")
    for i in range(n_tests):
        A = np.random.randint(-10, 11, (size, size))
        I = np.eye(size, dtype=int)
        
        left = np.dot(A + I, A - I)
        right = np.dot(A, A) - I
        difference = left - right
        
        print(f"Test {i+1}:")
        print("¿Es matriz nula?", np.array_equal(difference, np.zeros((size, size), dtype=int)))
        print(difference)
        print()

def test_identity_2():
    print("Testeando identidad (A + B)(A - B) = A^2 - B^2:")
    for i in range(n_tests):
        A = np.random.randint(-10, 11, (size, size))
        B = np.random.randint(-10, 11, (size, size))
        
        left = np.dot(A + B, A - B)
        right = np.dot(A, A) - np.dot(B, B)
        difference = left - right
        
        print(f"Test {i+1}:")
        print("¿Es matriz nula?", np.array_equal(difference, np.zeros((size, size), dtype=int)))
        print(difference)
        print()

test_identity_1()
test_identity_2()