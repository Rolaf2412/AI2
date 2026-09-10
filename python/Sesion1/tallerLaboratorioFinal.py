import numpy as np
#-------------------------------------------------------
# 1. Definir las matrices Imagen (I) y Kernel (K)
#-------------------------------------------------------
I = np.array([
    [100, 100, 100],
    [100, 200, 100],
    [100, 100, 100]
])

K = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])
#-------------------------------------------------------------------------
# 2. Calcular el Producto Hadamard (multiplicación elemento a elemento)
#-------------------------------------------------------------------------
producto_hadamard = I * K
#-------------------------------------------------------------------------
# 3. Sumar todos los valores para obtener el píxel central resultante
#-------------------------------------------------------------------------
pixel_central = np.sum(producto_hadamard)

# Imprimir el resultado
print("Matriz resultante del Producto Hadamard:\n", producto_hadamard)
print("\nEl valor del píxel central calculado es:", pixel_central)