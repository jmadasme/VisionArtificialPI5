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
        # Convertir el frame a escala de grises
        imagen_bn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Guardar la imagen en blanco y negro
        cv2.imwrite("captura_bn.jpg", imagen_bn)
        print("Fotografía en blanco y negro guardada como 'captura_bn.jpg'")
        break

camara.release()
cv2.destroyAllWindows()
