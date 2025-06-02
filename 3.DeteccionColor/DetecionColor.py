import cv2
import numpy as np

# Inicializar la cámara
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No se pudo abrir la cámara")
    exit()

print("Presiona 'q' para salir")

# Definir el rango de color HSV que queremos detectar
# Ejemplo: Rojo (ajustable para otros colores)
color_bajo = np.array([0, 120, 70])     # Valor mínimo del color (HSV)
color_alto = np.array([10, 255, 255])   # Valor máximo del color (HSV)

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al capturar imagen")
        break

    # Convertir la imagen de BGR (por defecto en OpenCV) a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear una máscara binaria donde estén los píxeles dentro del rango de color
    mascara = cv2.inRange(hsv, color_bajo, color_alto)

    # Encontrar los contornos en la máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 500:  # Filtramos objetos muy pequeños (ruido)
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Area: {int(area)}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Mostrar la imagen original con los rectángulos y la máscara
    cv2.imshow("Camara", frame)
    cv2.imshow("Mascara", mascara)

    # Salir al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
camara.release()
cv2.destroyAllWindows()
