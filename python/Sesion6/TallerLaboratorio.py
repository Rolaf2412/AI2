import cv2
import numpy as np

# 1. Cargar imagen en color
imagen_color = cv2.imread('python/Sesion6/image.png')

# Si no existe la imagen 'objetos.jpg', se genera una de prueba sintética con objetos
if imagen_color is None:
    imagen_color = np.zeros((400, 400, 3), dtype=np.uint8)
    # Objeto grande
    cv2.circle(imagen_color, (100, 100), 40, (255, 255, 255), -1)
    # Objeto pequeño
    cv2.circle(imagen_color, (300, 100), 15, (255, 255, 255), -1)
    # Objeto grande
    cv2.rectangle(imagen_color, (200, 250), (320, 350), (255, 255, 255), -1)

# 2. Pipeline de procesamiento: Grises -> Umbralización -> Limpieza Morfológica
imagen_grises = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)
_, imagen_binaria = cv2.threshold(imagen_grises, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)
imagen_limpia = cv2.morphologyEx(imagen_binaria, cv2.MORPH_OPEN, kernel)

# Detección de contornos
contornos, _ = cv2.findContours(imagen_limpia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Umbral para clasificar objeto grande/pequeño ("X" píxeles)
UMBRAL_AREA = 2000

# 3 y 4. Iterar sobre contornos y aplicar lógica empresarial
for cnt in contornos:
    area = cv2.contourArea(cnt)
    print(f"Área del objeto encontrado: {area} píxeles")
    
    x, y, w, h = cv2.boundingRect(cnt)
    
    if area > UMBRAL_AREA:
        # Bounding Box Azul para objeto grande
        cv2.rectangle(imagen_color, (x, y), (x + w, y + h), (255, 0, 0), 2)
    else:
        # Bounding Box Rojo para objeto pequeño
        cv2.rectangle(imagen_color, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Guardar la imagen final para revisar en Codespaces
cv2.imwrite('resultado_clasificacion.jpg', imagen_color)
print("Procesamiento finalizado. Resultado guardado en 'resultado_clasificacion.jpg'.")