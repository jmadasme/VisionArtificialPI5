import cv2

# Cargar el clasificador de rostros Haar Cascade
clasificador_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iniciar la cámara
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No se pudo abrir la cámara")
    exit()

print("Presiona 'q' para salir")

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al capturar imagen")
        break

    # Convertir a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros
    rostros = clasificador_rostro.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

    # Dibujar rectángulos alrededor de los rostros detectados
    for (x, y, w, h) in rostros:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar la imagen
    cv2.imshow("Detección de Rostros", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
camara.release()
cv2.destroyAllWindows()