import cv2

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No se puede acceder a la cámara")
    exit()

print("Cámara iniciada")
while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al capturar la imagen")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Guardar la imagen actual como 'captura.jpg'
        cv2.imwrite("captura.jpg", frame)
        print("Fotografía tomada y guardada como 'captura.jpg'")
        break

camara.release()
cv2.destroyAllWindows()
