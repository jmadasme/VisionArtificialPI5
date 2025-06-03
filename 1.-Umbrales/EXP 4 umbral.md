**EXPLICACIÓN DETALLADA**

**import cv2**

Se importa la biblioteca **OpenCV**, que permite trabajar con imágenes y
video en tiempo real.

**camara = cv2.VideoCapture(0)**

Inicia la cámara predeterminada del sistema (generalmente 0). Si
tuvieras varias cámaras podrías probar con 1, 2, etc.

**if not camara.isOpened():**

Verifica si la cámara pudo abrirse correctamente.

**exit()**

Si la cámara no se abrió, el programa termina inmediatamente.

**print("Presiona 'q' para salir")**

Muestra un mensaje indicando que puedes presionar la tecla **q** para
salir del programa.

**while True:**

Inicia un bucle infinito para procesar imágenes en tiempo real.

**ret, frame = camara.read()**

Captura un **frame (fotograma)** de la cámara.

-   ret: Booleano que indica si la captura fue exitosa.

-   frame: Es la imagen en color capturada (tipo BGR).

**if not ret:**

Si ret es falso, hubo un error al capturar y se sale del bucle.

**gris = cv2.cvtColor(frame, cv2.COLOR\_BGR2GRAY)**

Convierte el frame en color a **escala de grises**.

-   Esto reduce la imagen a una sola capa de intensidad de luz (sin
    colores).

-   Es útil para simplificar el procesamiento.

**\_, umbral = cv2.threshold(gris, 100, 255, cv2.THRESH\_BINARY\_INV)**

Esto aplica una **umbralización binaria inversa**:

-   Si un píxel en gris tiene valor **menor que 100**, el resultado es
    **blanco (255)**.

-   Si es **mayor o igual a 100**, el resultado es **negro (0)**.

-   El efecto es invertir los colores respecto al umbral.

**Parámetros:**

-   gris: imagen en escala de grises.

-   100: valor umbral.

-   255: valor asignado si se cumple la condición.

-   THRESH\_BINARY\_INV: tipo de umbralización **inversa**.

Esto es útil, por ejemplo, para resaltar una mano oscura sobre un fondo
claro.

**cv2.imshow("Original", frame)**

Muestra la imagen original en color.

**cv2.imshow("Gris", gris)**

Muestra la imagen convertida a escala de grises.

**cv2.imshow("Umbralizado", umbral)**

Muestra la imagen binarizada en blanco y negro invertido.

**if cv2.waitKey(1) & 0xFF == ord('q'):**

-   Espera 1 milisegundo por una tecla.

-   Si presionas 'q', rompe el bucle y termina el programa.

**camara.release()**

Libera la cámara (importante para que otros programas puedan usarla
después).

**cv2.destroyAllWindows()**

Cierra todas las ventanas abiertas por OpenCV.

**✅ ¿QUÉ HACE EL PROGRAMA?**

1.  Muestra en vivo:

    -   El video original.

    -   La versión en escala de grises.

    -   La versión umbralizada (blanco y negro invertido).

2.  Sirve para destacar **formas u objetos** según su luminosidad.

3.  Puedes usarlo como base para detectar **silhuetas**, **manos**,
    **movimientos**, etc.

4.  Presionando 'q', sales del programa.
