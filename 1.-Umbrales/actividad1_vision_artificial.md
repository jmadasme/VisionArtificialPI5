
# 🧠 Visión Artificial con Raspberry Pi – Actividad 1

## 📸 Umbralización y Detección de Bordes (Binarización de Imagen)

Esta actividad introduce una técnica fundamental en la visión artificial: la **umbralización** (también llamada binarización), que permite separar los objetos del fondo en una imagen en tiempo real, usando OpenCV y Python sobre una Raspberry Pi.

---

## 🎯 Objetivo

Transformar una imagen capturada por la cámara en una versión en blanco y negro puro (binaria) para facilitar la identificación de formas y objetos.

---

## 🧩 Código Base – Umbralización con OpenCV

```python
import cv2

# Inicializa la cámara (ID 0 = cámara por defecto)
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No se puede abrir la cámara")
    exit()

print("Presiona 'q' para salir")

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al capturar la imagen")
        break

    # Convertir a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral binario inverso
    _, umbral = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY_INV)

    # Mostrar resultados
    cv2.imshow("Original", frame)
    cv2.imshow("Gris", gris)
    cv2.imshow("Umbralizado", umbral)

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
camara.release()
cv2.destroyAllWindows()
```

---

## 🔍 Explicación detallada del código

### 1. `cv2.VideoCapture(0)`
Abre la cámara conectada. El número `0` indica la cámara por defecto (como una cámara USB o integrada en un portátil).

```python
camara = cv2.VideoCapture(0)
```

> Si la cámara no se abre correctamente, se detiene la ejecución con un mensaje de error.

---

### 2. Captura de fotogramas

```python
ret, frame = camara.read()
```

- `ret`: es `True` si se pudo capturar el fotograma correctamente.
- `frame`: es la imagen obtenida de la cámara en formato de color BGR (azul, verde, rojo).

---

### 3. Conversión a escala de grises

```python
gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

Convierte la imagen en color a escala de grises. Esto reduce la cantidad de información a procesar (1 solo canal en lugar de 3) y mejora la eficiencia.

🔹 **Ventaja**: la escala de grises permite trabajar directamente con la intensidad de luz.

---

### 4. Umbralización (binarización)

```python
_, umbral = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY_INV)
```

Esto convierte la imagen en blanco y negro puro:

- Todo píxel **con valor menor que 100** → blanco (`255`)
- Todo píxel **con valor igual o mayor que 100** → negro (`0`)
- El parámetro `THRESH_BINARY_INV` invierte este comportamiento para detectar objetos oscuros sobre fondo claro.

🎯 Ideal para separar figuras oscuras (como una tapa, un control, etc.) sobre un fondo iluminado.

---

### 5. Mostrar imágenes en pantalla

```python
cv2.imshow("Original", frame)
cv2.imshow("Gris", gris)
cv2.imshow("Umbralizado", umbral)
```

Se abren tres ventanas simultáneas:

| Ventana        | Contenido                        |
|----------------|----------------------------------|
| `Original`     | Imagen a color capturada         |
| `Gris`         | Imagen convertida a escala gris  |
| `Umbralizado`  | Imagen en blanco y negro binario |

---

### 6. Control de salida

```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```

Este comando escucha las teclas del teclado:
- Si se presiona `'q'`, se rompe el bucle y el programa termina.

---

### 7. Liberación de recursos

```python
camara.release()
cv2.destroyAllWindows()
```

Esto cierra correctamente la cámara y las ventanas de OpenCV.

---

## 📘 Conceptos clave

| Concepto         | Explicación                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Escala de grises | Imagen donde cada píxel representa solo la **intensidad de luz** (0 = negro, 255 = blanco).                                                     |
| Umbralización    | Técnica que convierte una imagen de grises en una imagen de solo **dos niveles** (blanco y negro) en función de un valor límite.                |
| THRESH_BINARY_INV| Variante que invierte el umbral: convierte lo oscuro en blanco y lo claro en negro.                                                            |
| Binarización     | Reducción de la imagen a solo dos colores para facilitar el análisis posterior.                                                                 |
| Segmentación     | Proceso de separar un objeto del fondo en una imagen, clave para reconocimiento de formas.                                                      |

---

## 📌 Consejos para una buena detección

- Usa un **fondo blanco o muy claro**.
- Usa un **objeto oscuro** con forma definida (control, bolígrafo, etc.).
- Asegúrate de tener **buena iluminación ambiental**.
- Puedes **ajustar el valor del umbral** (`100`) para mejorar resultados según las condiciones de luz.

---

## ✅ Resultado esperado

Al ejecutar el script:
- Verás la imagen original capturada en color.
- Una versión en escala de grises.
- Y una imagen binaria donde el objeto aparece **blanco sobre fondo negro**, ideal para análisis posterior.

---

## 🔜 ¿Qué sigue?

En la **Actividad 2**, aplicaremos **detección de contornos** a esta imagen binarizada para:
- **Detectar la silueta del objeto**.
- **Dibujar marcos o contornos** automáticamente.
- Calcular **área, centroide, forma**, etc.

---

> Esta actividad es el pilar inicial en visión artificial: toda tarea avanzada (detección de rostros, seguimiento de objetos, reconocimiento de patrones) comienza por una correcta segmentación de la imagen.

---

## 📁 Requisitos técnicos

- Raspberry Pi (o PC con Python 3)
- OpenCV instalado (`pip install opencv-python`)
- Cámara conectada y reconocida por el sistema

---

¿Dudas? ¿Resultados distintos? Revisa el umbral (`100`) y prueba con diferentes niveles de iluminación o distintos objetos.

---

📚 Curso de Visión Artificial con Raspberry Pi  
📅 Módulo 1 – Fundamentos de Captura y Procesamiento  
👨‍🏫 Profesor: [Tu Nombre]
