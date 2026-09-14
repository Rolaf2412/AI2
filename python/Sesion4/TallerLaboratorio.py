import cv2
import numpy as np

# Cargar imagen con ruido sintético o real
imagen = cv2.imread('python/Sesion4/image.png')

# 1. Filtro de Media (Promedio simple 7x7)
blur_media = cv2.blur(imagen, (7, 7))

# 2. Filtro Gaussiano (Kernel 7x7, desviación estándar calculada auto)
blur_gauss = cv2.GaussianBlur(imagen, (7, 7), 0)

# 3. Filtro de Mediana (Excelente para ruido de impulso/Sal y Pimienta)
# Solo recibe un número impar entero para el tamaño del Kernel
blur_mediana = cv2.medianBlur(imagen, 7)

# Guardar los resultados para verlos en el explorador de Codespaces
cv2.imwrite('resultado_media.jpg', blur_media)
cv2.imwrite('resultado_gauss.jpg', blur_gauss)
cv2.imwrite('resultado_mediana.jpg', blur_mediana)

print("Imágenes guardadas correctamente en Codespaces.")