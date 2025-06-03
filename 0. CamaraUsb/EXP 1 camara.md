**EXPLICACIÓN DETALLADA**

**import cv2**

**¿Qué hace?**\
Importa la biblioteca **OpenCV**, que es una herramienta poderosa para
visión por computadora.

**camara = cv2.VideoCapture(0)**

**¿Qué hace?**\
Crea un objeto llamado camara que se conecta a una **fuente de video**.

-   cv2.VideoCapture(0) intenta acceder a la **cámara por defecto** del
    sistema (por ejemplo, la webcam).

-   Si tienes varias cámaras, puedes usar 1, 2, etc. para otras cámaras
    externas.

**if not camara.isOpened():**

**¿Qué hace?**\
Verifica si la cámara se abrió correctamente.

**print("So se peude cacder camara")**

**Nota:** Hay un **error tipográfico** en el mensaje. Lo correcto sería:

python

Copiar código

print("No se puede acceder a la cámara")

**exit()**

**¿Qué hace?**\
Si no se pudo abrir la cámara, termina inmediatamente el programa.

**print("Camara iniciada")**

**¿Qué hace?**\
Confirma que la cámara fue detectada y está lista para usarse.

**while True:**

**¿Qué hace?**\
Bucle infinito: el programa entra en un ciclo que solo se detiene cuando
tú lo indicas.

**ret, frame = camara.read()**

**¿Qué hace?**\
Captura un **fotograma (frame)** de la cámara.

-   ret: es un booleano que indica si la captura fue exitosa (True) o
    falló (False).

-   frame: es una **matriz de píxeles (imagen)** que representa el
    fotograma capturado.

**if not ret:**

**¿Qué hace?**\
Verifica si hubo un error al capturar el fotograma. Si ret es False,
termina el bucle.

**cv2.imshow("video", frame)**

**¿Qué hace?**\
Muestra la imagen capturada en una **ventana** llamada "video".

La ventana se actualiza con cada nuevo fotograma capturado.

**if cv2.waitKey(1) & 0xFF == ord('q'):**

**¿Qué hace?**

-   cv2.waitKey(1) espera 1 milisegundo por una tecla.

-   ord('q') es el código ASCII de la tecla 'q'.

-   Si presionas 'q', el programa **sale del bucle**.

**camara.release()**

**¿Qué hace?**\
Libera el objeto cámara. Muy importante para que no quede ocupada por
este script.

**cv2.destroyAllWindows()**

**¿Qué hace?**\
Cierra todas las ventanas abiertas por OpenCV.

**✅ ¿Qué hace este programa?**

Este código abre la cámara, captura imágenes en tiempo real, las muestra
en pantalla, y permite detener la ejecución presionando la tecla 'q'.
