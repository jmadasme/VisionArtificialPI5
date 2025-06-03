**EXPLICACIÓN DETALLADA**

**import cv2**

Importa la biblioteca **OpenCV**, que te permite trabajar con visión por
computadora, imágenes, video, etc.

**camara = cv2.VideoCapture(0)**

-   Abre la **cámara predeterminada** del sistema (usualmente la webcam
    integrada o conectada por USB).

-   Si tienes otra cámara, puedes probar con 1, 2, etc.

**if not camara.isOpened():**

Verifica si la cámara se pudo abrir correctamente.

**print("No se puede acceder a la cámara")**

Mensaje en caso de fallo.

(En tu código original tenías caracteres raros: Ã¡. Eso es un problema
de codificación UTF-8 mal interpretado).

**exit()**

Sale del programa si no se pudo abrir la cámara.

**print("Cámara iniciada")**

Confirma que la cámara está funcionando correctamente.

**while True:**

Bucle infinito: captura y muestra los fotogramas hasta que se presione
la tecla 'q'.

**ret, frame = camara.read()**

-   ret: indica si se pudo capturar un fotograma (True) o no (False).

-   frame: contiene la imagen del fotograma capturado.

**if not ret:**

Si no se pudo capturar la imagen, termina el bucle.

**cv2.imshow("Video", frame)**

Muestra el video en tiempo real en una ventana llamada "Video".

**if cv2.waitKey(1) & 0xFF == ord('q'):**

-   Espera 1 milisegundo por una tecla.

-   Si presionas la tecla 'q', entra en este bloque.

**cv2.imwrite("captura.jpg", frame)**

Guarda la imagen actual (frame) como un archivo JPEG con el nombre
"captura.jpg" en el mismo directorio donde se ejecuta el script.

**print("Fotografía tomada y guardada como 'captura.jpg'")**

Mensaje que indica que la foto fue tomada y guardada correctamente.

**break**

Sale del bucle para terminar la ejecución del programa.

**camara.release()**

Libera la cámara para que pueda ser usada por otros programas.

**cv2.destroyAllWindows()**

Cierra todas las ventanas creadas por OpenCV.

**✅ ¿QUÉ HACE ESTE PROGRAMA?**

1.  Abre la cámara.

2.  Muestra video en tiempo real.

3.  Al presionar 'q':

    -   Captura una imagen.

    -   La guarda como "captura.jpg".

    -   Sale del programa.
