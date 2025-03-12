import numpy as np

# Definir la matriz A de coeficientes
A = np.array([
    [3, -2, 5, -1, 4, 2, -3, 1, 2],
    [-2, 4, -3, 1, 5, -1, 2, -4, 3],
    [5, -1, 2, -3, 4, 1, -2, 3, -1],
    [1, -3, 4, -2, 5, -1, 2, -1, 4],
    [2, 3, -1, 4, -2, 5, -3, 1, -2],
    [-3, 2, 4, -1, 3, -2, 5, -1, 1],
    [4, -1, 3, 2, -3, 1, -2, 5, -4],
    [-1, 5, -2, 3, 4, -1, 2, -3, 1],
    [3, -2, 5, -1, 4, 2, -3, 1, -5]
])

# Definir el vector b de resultados
b = np.array([-8, 7, -6, 5, 12, -9, 10, 3, -2])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(A, b)

# Mostrar los resultados
print("Las soluciones para las x^ son:")
for i in range(len(x)):
    print(f"x{i+1} = {x[i]}")
