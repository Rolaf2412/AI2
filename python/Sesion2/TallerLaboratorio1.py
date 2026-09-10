import numpy as np
import cv2
#----------------------------------------
# 1.Crear el pixel
#----------------------------------------
Pixel = np.array([0,255,255])
#----------------------------------------
# 2. Escala de grises
#----------------------------------------
producto_punto = np.array([0.114, 0.587, 0.299])
Pixel_Grises =  np.dot(Pixel,producto_punto)
#----------------------------------------
# 3. Imprimir el resultado
#----------------------------------------
print(f"Valor de grises: {Pixel_Grises}")
#----------------------------------------
# 4. Uso de OpenCV
#----------------------------------------
# Leer la imagen subida
imagen = cv2.imread("python/Sesion2/image.png")

if imagen is not None:
    # Convertir a escala de grises
    img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Guardar la imagen en el directorio de trabajo
    cv2.imwrite("resultado_gris.jpg", img_gris)
    print("Imagen guardada exitosamente como 'resultado_gris.jpg'")
else:
    print("No se encontró la imagen original.")