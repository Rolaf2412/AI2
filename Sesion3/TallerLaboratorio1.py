import cv2
import numpy as np

# 1. Cargar la imagen en escala de grises
imagen_gris = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

if imagen_gris is None:
    print("Error: No se encontró la imagen 'imagen_real.jpg'.")
else:
    # 2. Umbralización binaria estática (genera algo de ruido intencional)
    # Ajusta el valor 120 según el nivel de contraste de tu imagen
    umbral = 120
    _, img_binaria = cv2.threshold(
        imagen_gris, umbral, 255, cv2.THRESH_BINARY
    )
    cv2.imwrite("1_binaria_con_ruido.png", img_binaria)

    # 3. Construir un Elemento Estructurante (Kernel) de 3x3
    kernel = np.ones((3, 3), np.uint8)

    # 4. Operación Morfológica de Apertura (Erosión -> Dilatación)
    # Limpia el ruido blanco en el fondo (ruido de sal)
    img_apertura = cv2.morphologyEx(
        img_binaria, cv2.MORPH_OPEN, kernel
    )  # Equivale a cv2.dilate(cv2.erode(img_binaria, kernel), kernel)
    cv2.imwrite("2_apertura.png", img_apertura)

    # 5. Operación Morfológica de Cierre (Dilatación -> Erosión)
    # Rellena huecos negros dentro del objeto (ruido de pimienta)
    img_cierre = cv2.morphologyEx(
        img_binaria, cv2.MORPH_CLOSE, kernel
    )  # Equivale a cv2.erode(cv2.dilate(img_binaria, kernel), kernel)
    cv2.imwrite("3_cierre.png", img_cierre)

    print("Proceso completado. Se guardaron las tres imágenes en tu workspace:")
    print(" - 1_binaria_con_ruido.png")
    print(" - 2_apertura.png")
    print(" - 3_cierre.png")