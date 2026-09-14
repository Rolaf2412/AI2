import cv2
import numpy as np

# 1. Cargar imagen en escala de grises
imagen = cv2.imread('python/Sesion5/image.png', cv2.IMREAD_GRAYSCALE)

# Si no existe la imagen 'python/Sesion5/image.png', se genera una de prueba sintética
if imagen is None:
    imagen = np.zeros((300, 300), dtype=np.uint8)
    cv2.rectangle(imagen, (50, 50), (250, 250), 255, -1)
    cv2.circle(imagen, (150, 150), 60, 100, -1)

# 2. Bordes con Sobel X y Sobel Y
sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)

sobel_x_abs = cv2.convertScaleAbs(sobel_x)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

# 3. Bordes con Canny (Umbrales por defecto, bajos y altos)
canny_estandar = cv2.Canny(imagen, 50, 150)
canny_bajo = cv2.Canny(imagen, 10, 50)
canny_alto = cv2.Canny(imagen, 200, 250)

# 4. Guardar resultados para revisar en el explorador de Codespaces
cv2.imwrite('sobel_x.jpg', sobel_x_abs)
cv2.imwrite('sobel_y.jpg', sobel_y_abs)
cv2.imwrite('canny_estandar.jpg', canny_estandar)
cv2.imwrite('canny_bajo.jpg', canny_bajo)
cv2.imwrite('canny_alto.jpg', canny_alto)

print("Procesamiento finalizado. Archivos .jpg guardados en la carpeta raíz.")