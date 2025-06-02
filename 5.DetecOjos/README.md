
# 👁️‍🗨️ Actividad 4: Detección de Rostros y Ojos con OpenCV

## 🎯 Objetivo

Detectar **rostros humanos** y sus **ojos** en tiempo real usando la cámara web, gracias a OpenCV y los clasificadores Haar Cascade. Este conocimiento es base en proyectos como:

- Sistemas de vigilancia.
- Reconocimiento facial.
- Interfaces hombre-máquina.
- Dispositivos de asistencia.

---

## 🧠 ¿Qué es un clasificador Haar Cascade?

Un **clasificador Haar Cascade** es un archivo entrenado (modelo XML) capaz de **detectar objetos específicos** (como rostros u ojos) en imágenes, basado en un conjunto de características (o "ondas Haar").

Para entrenarlo, se usa:
- **Imágenes positivas** (con el objeto a detectar).
- **Imágenes negativas** (sin el objeto).

OpenCV ya incluye clasificadores preentrenados para:
- Rostros.
- Ojos.
- Sonrisas.
- Cuerpos completos.
- Matrículas de autos, etc.

---

## 🔧 Requisitos

Antes de comenzar, asegúrate de tener:

- Python 3.8 o superior.
- OpenCV instalado:  
  ```bash
  pip install opencv-python
  ```
- Archivos Haar Cascade incluidos con OpenCV:
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_eye.xml`

---

## 💻 Código Python: Detección de Rostros y Ojos

```python
import cv2

# 1. Cargar clasificadores Haar
clasificador_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
clasificador_ojos = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 2. Iniciar la cámara web
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("No se pudo acceder a la cámara")
    exit()

print("Presiona 'q' para salir")

# 3. Bucle de captura de video
while True:
    ret, frame = cam.read()
    if not ret:
        print("Error al capturar imagen")
        break

    # 4. Convertir imagen a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Detectar rostros
    rostros = clasificador_rostros.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in rostros:
        # 6. Dibujar rectángulo en el rostro
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Rostro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # 7. Crear una región de interés (ROI) dentro del rostro
        rostro_gris = gris[y:y + h, x:x + w]
        rostro_color = frame[y:y + h, x:x + w]

        # 8. Detectar ojos dentro de esa ROI
        ojos = clasificador_ojos.detectMultiScale(rostro_gris, scaleFactor=1.1, minNeighbors=10)

        for (ox, oy, ow, oh) in ojos:
            # 9. Dibujar rectángulo en cada ojo
            cv2.rectangle(rostro_color, (ox, oy), (ox + ow, oy + oh), (255, 0, 0), 2)
            cv2.putText(rostro_color, "Ojo", (ox, oy - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # 10. Mostrar imagen con las detecciones
    cv2.imshow("Rostros y Ojos Detectados", frame)

    # 11. Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 12. Liberar recursos
cam.release()
cv2.destroyAllWindows()
```

---

## 🧩 Explicación del Código

1. `import cv2`  
   Importa la librería OpenCV, fundamental para la visión artificial.

2. `CascadeClassifier`  
   Carga los clasificadores XML para rostros y ojos.

3. `VideoCapture(0)`  
   Inicia la cámara web (índice 0 suele ser la cámara principal).

4. `cvtColor(...)`  
   Convierte cada fotograma a escala de grises para facilitar el procesamiento.

5. `detectMultiScale(...)`  
   Detecta rostros u ojos dentro de una imagen (o subimagen).

6. `rectangle(...)` y `putText(...)`  
   Dibuja marcos y etiquetas sobre la imagen original.

7. **Región de interés (ROI)**  
   Optimiza la búsqueda de ojos dentro del área donde se encontró un rostro.

8. `imshow(...)`  
   Muestra el resultado final con las detecciones en una ventana.

9. `waitKey(...) + ord('q')`  
   Espera entrada del teclado. Si se presiona `q`, sale del bucle.

10. `release()` y `destroyAllWindows()`  
    Libera la cámara y cierra las ventanas para evitar errores.

---

## 🧪 Actividades Sugeridas

- Detecta sonrisas con `haarcascade_smile.xml`.
- Cambia el color del marco o el texto.
- Guarda las imágenes detectadas con `cv2.imwrite(...)`.
- Usa una imagen estática o una cámara IP.
- Implementa un sistema que tome asistencia al detectar rostros.

---

## 📎 Recursos útiles

- [Documentación oficial de OpenCV](https://docs.opencv.org/)
- [Clasificadores Haar en GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- [Curso introductorio de OpenCV en Python](https://opencv.org/)

---

¡Ahora ya puedes detectar rostros y ojos en tiempo real! Esta base te servirá para proyectos de inteligencia artificial, seguridad, IoT y domótica.
