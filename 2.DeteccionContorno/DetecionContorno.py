import cv2

# Inicializa la cámara
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No se puede abrir la cámara")
    exit()

print("Presiona 'q' para salir")

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al capturar imagen")
        break

    # Convertir a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Umbralización (binarización)
    _, binaria = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY_INV)

    # Detección de contornos
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 500:  # Filtrar "ruido" por área mínima
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Marco verde
            cv2.putText(frame, f"Area: {int(area)}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Mostrar resultados
    cv2.imshow("Camara", frame)
    cv2.imshow("Binaria", binaria)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
