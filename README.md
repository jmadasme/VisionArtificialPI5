## Guía de Instalación

Sigue estos pasos para configurar tu entorno:

1.  **Instala el soporte para entornos virtuales** (si aún no lo tienes):
    ```bash
    sudo apt install python3-venv python3-full
    ```

2.  **Crea un entorno virtual**:
    ```bash
    python3 -m venv camopencv
    ```

3.  **Activa el entorno virtual**:
    ```bash
    source camopencv/bin/activate
    ```
    Tu prompt debería cambiar para indicar que estás dentro del entorno virtual, algo como: `(camopencv) jma@raspberrypi:~ $`

4.  **Instala paquetes dentro del entorno virtual**:
    ```bash
    pip install opencv-python numpy
    sudo apt install python3-opencv python3-pip
    ```

