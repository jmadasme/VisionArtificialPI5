import cv2

# Cargar clasificadores Haar Cascade
clasificador_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
clasificador_ojos = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Iniciar cámara
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("No se pudo acceder a la cámara")
    exit()

print("Presiona 'q' para salir")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Error al capturar imagen")
        break

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = clasificador_rostros.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in rostros:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Rostro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Área de interés para los ojos dentro del rostro
        rostro_gris = gris[y:y + h, x:x + w]
        rostro_color = frame[y:y + h, x:x + w]
        ojos = clasificador_ojos.detectMultiScale(rostro_gris, scaleFactor=1.1, minNeighbors=10)

        for (ox, oy, ow, oh) in ojos:
            cv2.rectangle(rostro_color, (ox, oy), (ox + ow, oy + oh), (255, 0, 0), 2)
            cv2.putText(rostro_color, "Ojo", (ox, oy - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    cv2.imshow("Rostros y Ojos Detectados", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
