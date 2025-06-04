**Cómo cambiar el nombre de host de tu Raspberry Pi 5**

¡Sí, es totalmente posible asignar un nombre de host a tu Raspberry Pi 5! De hecho, es una de las primeras cosas que se recomienda hacer para facilitar la identificación y el acceso a tu dispositivo en la red. Por defecto, todas las Raspberry Pi vienen con el nombre de host "raspberrypi", lo que puede generar confusiones si tienes varias en tu red.

Hay varias formas de cambiar el nombre de host en una Raspberry Pi 5:

-----
**1. Usando hostnamectl (Método recomendado en línea de comandos)**

Este es el método más moderno y recomendado para sistemas basados en systemd, como Raspberry Pi OS.

Bash

sudo hostnamectl set-hostname TU\_NUEVO\_HOSTNAME

**Ejemplo:** Si quieres que tu Raspberry Pi se llame pilocala, ejecutarías:

Bash

sudo hostnamectl set-hostname pilocala

Después de ejecutar este comando, el nombre de host se actualizará de inmediato. Sin embargo, es posible que necesites **reiniciar la sesión de la terminal o la Raspberry Pi** para que el nuevo nombre se refleje en el *prompt* de la terminal y en otros servicios de red.

-----
**2. Usando raspi-config (Herramienta de configuración de Raspberry Pi)**

Esta es una interfaz basada en texto muy útil para configurar varias opciones en tu Raspberry Pi.

1. Abre la herramienta raspi-config en la terminal: 

   Bash

   sudo raspi-config

1. Navega a "**Network Options**" (Opciones de red).
1. Selecciona "**Hostname**".
1. Introduce tu **nuevo nombre de host** (solo letras, números y guiones, sin espacios) y presiona Enter.
1. Acepta los cambios y, cuando se te pregunte, **reinicia** tu Raspberry Pi.
-----
**3. Editando archivos de configuración directamente**

Este método es para aquellos que prefieren modificar los archivos directamente.

1. **Edita /etc/hostname:** Este archivo contiene solo el nombre de host.

   Bash

   sudo nano /etc/hostname

   Borra el nombre existente y escribe tu **TU\_NUEVO\_HOSTNAME**. Guarda el archivo (**Ctrl+X**, luego Y, luego Enter).

1. **Edita /etc/hosts:** Este archivo mapea nombres de host a direcciones IP locales. Debes asegurarte de que tu nuevo nombre de host también esté presente aquí para la dirección 127.0.1.1.

   Bash

   sudo nano /etc/hosts

   Busca la línea que comienza con 127.0.1.1 y cambia el nombre de host antiguo por el nuevo. Por ejemplo, si antes decía 127.0.1.1 raspberrypi, cámbialo a 127.0.1.1 TU\_NUEVO\_HOSTNAME. Guarda el archivo (**Ctrl+X**, luego Y, luego Enter).

1. **Reinicia la Raspberry Pi:** Para que los cambios surtan efecto en todo el sistema.

   Bash

   sudo reboot

-----
**Consideraciones adicionales:**

- **Sin caracteres especiales ni espacios:** Los nombres de host solo deben contener letras (a-z), números (0-9) y guiones (-). No uses espacios ni otros caracteres especiales.
- **.local en la red:** Una vez que cambies el nombre de host, podrás acceder a tu Raspberry Pi en tu red local utilizando el nuevo nombre seguido de .local (por ejemplo, ssh pi@pilocala.local o ping pilocala.local), siempre y cuando tu *router* y otros dispositivos de tu red soporten mDNS (Multicast DNS, a menudo implementado por Avahi en Linux).
- **Reiniciar es clave:** Aunque hostnamectl actualiza el nombre de host inmediatamente, un reinicio asegura que todos los servicios y aplicaciones que se ejecutan en la Raspberry Pi reconozcan el nuevo nombre.

Personalmente, el método hostnamectl es el más rápido y directo si estás en la terminal. Si prefieres una interfaz gráfica, raspi-config es una excelente opción.

