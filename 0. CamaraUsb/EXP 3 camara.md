**EXPLICACIÓN DETALLADA**

**import cv2**

Importa la biblioteca **OpenCV**, que sirve para trabajar con imágenes,
video, visión por computadora, etc.

**camara = cv2.VideoCapture(0)**

Intenta abrir la **cámara número 0**, que es normalmente la cámara por
defecto del sistema (puede ser integrada o USB).

**if not camara.isOpened():**

Verifica que la cámara se haya abierto correctamente.

**exit()**

Si la cámara no se pudo abrir, el programa se detiene aquí.

**print("Cámara iniciada")**

Muestra un mensaje indicando que la cámara se abrió correctamente.

**while True:**

Inicia un bucle infinito para capturar fotogramas en tiempo real.

**ret, frame = camara.read()**

-   ret: Booleano que indica si la captura fue exitosa.

-   frame: Imagen capturada por la cámara (una matriz con valores RGB).

**if not ret:**

Si la imagen no se pudo capturar, se imprime un mensaje de error y se
rompe el bucle.

**cv2.imshow("Video", frame)**

Muestra el fotograma actual en una ventana llamada "Video".

**if cv2.waitKey(1) & 0xFF == ord('q'):**

-   Espera 1 ms por una tecla.

-   Si se presiona la tecla 'q', ejecuta el siguiente bloque.

**imagen\_bn = cv2.cvtColor(frame, cv2.COLOR\_BGR2GRAY)**

-   Convierte la imagen de color (BGR) a escala de grises.

-   COLOR\_BGR2GRAY es una constante de OpenCV que indica la
    transformación deseada.

-   El resultado es una imagen en blanco y negro (solo un canal de
    intensidad).

**cv2.imwrite("captura\_bn.jpg", imagen\_bn)**

Guarda la imagen en blanco y negro como "captura\_bn.jpg" en el mismo
directorio donde ejecutas el script.

**print("Fotografía en blanco y negro guardada como
'captura\_bn.jpg'")**

Mensaje para confirmar que la foto fue guardada correctamente.

**break**

Rompe el bucle y termina la ejecución.

**camara.release()**

Libera la cámara (por si otro programa la quiere usar después).

**cv2.destroyAllWindows()**

Cierra todas las ventanas de OpenCV.

**✅ ¿QUÉ HACE ESTE PROGRAMA?**

1.  Abre la cámara y muestra video en vivo.

2.  Si presionas 'q':

    -   Convierte el fotograma actual a blanco y negro.

    -   Guarda la imagen como "captura\_bn.jpg".

    -   Cierra todo y termina el programa.
