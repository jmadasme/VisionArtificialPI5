
# 🧠 Actividad 3 - Detección de Color con OpenCV

## 🎯 Objetivo

Detectar objetos en una imagen basándonos **específicamente en su color**, utilizando el modelo de color HSV. Aprenderemos a aplicar filtros por color y segmentar regiones relevantes, dibujando marcos sobre los objetos detectados.

---

## 🧰 Herramientas

- Raspberry Pi (o cualquier PC con cámara)
- Python 3
- OpenCV (`cv2`)
- Numpy (`np`)

---

## 📚 Fundamentos Teóricos

### ¿Por qué usar HSV y no BGR o RGB?
El modelo **HSV** (Hue, Saturation, Value) es más adecuado para detectar colores, ya que **separa la información del color (matiz)** de la **iluminación (valor)**.

| Canal | Significado |
|-------|-------------|
| H (Hue) | Tono (color puro), de 0 a 179 en OpenCV |
| S (Saturation) | Saturación, qué tan puro o vivo es el color |
| V (Value) | Valor, qué tan claro u oscuro es el color |

Usar HSV permite detectar colores **sin importar sombras o luz intensa**, lo cual es muy útil para condiciones variables del entorno.

---

## 🖼️ ¿Qué vamos a hacer?

1. Tomar imagen en tiempo real de la cámara.
2. Convertir de BGR a HSV.
3. Aplicar una máscara para detectar un color específico.
4. Dibujar un marco verde alrededor de las regiones detectadas.
5. Mostrar la imagen original, la máscara y el resultado en tiempo real.

---

## 🧾 Código completo

```python
import cv2
import numpy as np

# Inicializar la cámara
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No se pudo abrir la cámara")
    exit()

print("Presiona 'q' para salir")

# Rango de color a detectar (por ejemplo: rojo)
# Puedes ajustar estos valores para detectar otros colores
color_bajo = np.array([0, 120, 70])     # HSV mínimo
color_alto = np.array([10, 255, 255])   # HSV máximo

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al capturar imagen")
        break

    # Convertimos la imagen de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Creamos una máscara para el color deseado
    mascara = cv2.inRange(hsv, color_bajo, color_alto)

    # Encontrar contornos en la máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Area: {int(area)}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Mostrar imágenes
    cv2.imshow("Camara", frame)
    cv2.imshow("Mascara", mascara)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
```

---

## 🔍 Explicación del Código

### 1. Conversión de color
```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```
La cámara da imágenes en BGR. Las convertimos a HSV para trabajar mejor con colores.

### 2. Máscara por color
```python
mascara = cv2.inRange(hsv, color_bajo, color_alto)
```
Creamos una **máscara binaria** que deja en blanco los píxeles del color deseado y en negro el resto.

### 3. Contornos
```python
contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```
Buscamos los bordes de las regiones blancas (el color que buscamos).

### 4. Dibujar rectángulos
```python
cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
```
Enmarcamos el objeto del color detectado con un rectángulo verde.

---

## 🎨 ¿Cómo detectar otros colores?

| Color | Rango HSV aproximado |
|-------|----------------------|
| Rojo  | `[0, 120, 70]` a `[10, 255, 255]` y `[170, 120, 70]` a `[180, 255, 255]` (rojo está en dos zonas) |
| Verde | `[36, 100, 100]` a `[86, 255, 255]` |
| Azul  | `[94, 80, 2]` a `[126, 255, 255]` |
| Amarillo | `[15, 150, 150]` a `[35, 255, 255]` |

Puedes probar cambiando los valores de `color_bajo` y `color_alto` para experimentar.

---

## 🧠 ¿Qué aprendimos?

- A segmentar objetos según su color en imágenes.
- Cómo el modelo HSV permite detectar colores de forma más robusta.
- A trabajar con máscaras, operaciones bit a bit y contornos.

---

## ✅ Resultado Esperado

Verás una cámara en tiempo real donde los objetos del color especificado aparecerán rodeados por marcos verdes. También podrás ver la **máscara binaria** que muestra qué partes fueron detectadas.

---

## 📘 Actividad siguiente

En la **Actividad 4**, mejoraremos esta segmentación con **operaciones morfológicas** (como erosión y dilatación), para eliminar ruido y mejorar precisión.

