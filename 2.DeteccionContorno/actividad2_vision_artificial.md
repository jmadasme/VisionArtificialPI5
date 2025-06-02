
# 🧠 Actividad 2 - Detección de Contornos con OpenCV

## 🎯 Objetivo

Detectar automáticamente los contornos de los objetos presentes en la imagen obtenida por la cámara web, encerrar estos objetos en **marcos verdes** y mostrar información básica como el área de cada contorno.

---

## 🧰 Herramientas

- Raspberry Pi (o cualquier PC con cámara)
- Python 3
- OpenCV (`cv2`)
- Numpy (instalado junto con OpenCV)

---

## 🔍 Conceptos Clave

| Concepto             | Explicación |
|----------------------|------------|
| `cv2.findContours`   | Encuentra los bordes cerrados (contornos) en una imagen binaria. |
| `cv2.drawContours`   | Dibuja los contornos detectados sobre la imagen. |
| `cv2.boundingRect`   | Calcula un rectángulo que encierra completamente un contorno. |
| `cv2.contourArea`    | Calcula el área del contorno. Sirve para filtrar objetos pequeños o ruido. |
| `cv2.threshold`      | Realiza una binarización sobre una imagen en escala de grises. |

---

## 🧾 Código completo

```python
import cv2

# Inicializa la cámara
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No se puede abrir la cámara")
    exit()

print("Presiona 'q' para salir")

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al capturar imagen")
        break

    # Convertir a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Umbralización (binarización)
    _, binaria = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY_INV)

    # Detección de contornos
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 500:  # Filtrar "ruido" por área mínima
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Marco verde
            cv2.putText(frame, f"Area: {int(area)}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Mostrar resultados
    cv2.imshow("Camara", frame)
    cv2.imshow("Binaria", binaria)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
```

---

## 🧠 Explicación del código

- **Conversión a escala de grises:** facilita el procesamiento al reducir la información de color.
- **Binarización:** permite distinguir el objeto del fondo (objeto blanco sobre fondo negro o viceversa).
- **Detección de contornos:** busca líneas cerradas en la imagen binarizada.
- **Cálculo de área:** se descartan contornos demasiado pequeños (ruido).
- **Rectángulo verde:** se dibuja un marco visible sobre el objeto detectado.
- **Mostrar área:** útil para estudiar tamaños relativos de los objetos.

---

## 📌 Propósito de la actividad

- Comprender cómo se representan los objetos mediante contornos.
- Introducir funciones clave de OpenCV para análisis estructural de imágenes.
- Aplicar filtros lógicos como el área mínima para una detección más precisa.
- Empezar a "interpretar" escenas mediante análisis geométrico.

---

## 💡 Recomendaciones

- Asegúrate de tener buena iluminación.
- Usa objetos oscuros sobre fondo claro o viceversa.
- Si se detecta mucho ruido, incrementa el área mínima (`area > 1000`, por ejemplo).
- También puedes ajustar el umbral de binarización para mejorar los resultados.

---

## ✅ Resultado esperado

Una ventana en tiempo real donde se muestra la cámara con marcos verdes alrededor de los objetos detectados y su respectiva área.

---

## 📚 Continuación

En la **Actividad 3**, usaremos esta base para detectar colores específicos, o aplicar filtros morfológicos para mejorar la segmentación.

