import cv2
import matplotlib.pyplot as plt

# 1. Cargar la imagen en Python
# Asegúrate de reemplazar 'imagen_real.jpg' por el nombre de tu archivo
imagen = cv2.imread("python/Sesion2/image.png")

if imagen is None:
    print(
        "Error: No se encontró la imagen. Verfica el nombre y la ruta del archivo."
    )
else:
    # 2. Separar la imagen en sus 3 canales (B, G, R)
    b, g, r = cv2.split(imagen)

    # Nombres de canales y colores para graficar
    canales = (b, g, r)
    colores = ("b", "g", "r")
    etiquetas = ("Canal Azul (Blue)", "Canal Verde (Green)", "Canal Rojo (Red)")

    # Crear la figura de Matplotlib
    plt.figure(figsize=(10, 5))
    plt.title("Histograma de Canales de Color (BGR)")
    plt.xlabel("Intensidad del Píxel (0 - 255)")
    plt.ylabel("Número de Píxeles")

    # 3 y 4. Calcular el histograma de cada canal y graficarlos superpuestos
    for canal, color, etiqueta in zip(canales, colores, etiquetas):
        # cv2.calcHist([images], [channels], mask, histSize, ranges)
        hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
        plt.plot(hist, color=color, label=etiqueta)

    plt.xlim([0, 256])
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # Guardar la gráfica para verla en Codespaces
    plt.savefig("histograma_canales.png")
    plt.close()
    print(
        "Gráfica guardada exitosamente como 'histograma_canales.png' en tu workspace."
    )