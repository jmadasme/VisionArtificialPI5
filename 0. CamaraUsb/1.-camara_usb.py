import cv2

camara=cv2.VideoCapture(0)
if not camara.isOpened():
    print("So se peude cacder camara")
    exit()
print("Camara iniciada")
while True:
	ret, frame= camara.read()
	if not ret:
		print("Erro al capturar la imagen")
		break
	cv2.imshow("video",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
camara.release()
cv2.destroyAllWindows()

