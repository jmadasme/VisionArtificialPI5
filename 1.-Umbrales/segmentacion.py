import cv2

# Iniciar la cámara
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No se puede abrir la cámara")
    exit()

print("Presiona 'q' para salir")

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al capturar la imagen")
        break

    # Escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Umbralización (binaria)
    _, umbral = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY_INV)

    # Mostrar imágenes
    cv2.imshow("Original", frame)
    cv2.imshow("Gris", gris)
    cv2.imshow("Umbralizado", umbral)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
