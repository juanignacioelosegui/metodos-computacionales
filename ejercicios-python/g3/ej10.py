import numpy as np

# a) Matriz nxm de ceros
def a (n:int, m:int):
    return np.zeros((n, m))

# b) Matriz nxm de unos
def b (n:int, m:int):
    return np.ones((n, m))

# c) Matriz identidad de nxn
def c (n:int):
    return np.identity(n)

# d) Matriz diagonal de nxn con elementos diagonales pasados como parametro
def d (v:list[int]):
    return np.diag(v)