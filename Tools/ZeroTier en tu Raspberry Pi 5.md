Aquí tienes los comandos para instalar el cliente ZeroTier en tu Raspberry Pi 5. Estos comandos asumen que tienes instalado Raspberry Pi OS y que tu sistema está actualizado.

**1. Actualiza tu sistema (recomendado):**

Abre una terminal y ejecuta:

Bash

sudo apt update

sudo apt upgrade -y

**2. Instala ZeroTier:**

La forma más sencilla y recomendada es usar el script de instalación de ZeroTier. Hay dos opciones:

- **Opción 1: Instalación sencilla (menos segura, pero funciona):**

  Bash

  curl -s https://install.zerotier.com | sudo bash

- **Opción 2: Instalación más segura con verificación GPG (recomendado):**

  Bash

  curl -s 'https://raw.githubusercontent.com/zerotier/ZeroTierOne/main/doc/contact%40zerotier.com.gpg' | gpg --import && \

  if z=$(curl -s 'https://install.zerotier.com/' | gpg); then echo "$z" | sudo bash; fi

  Después de usar cualquiera de los scripts, puedes usar apt para futuras actualizaciones.

**3. Une tu Raspberry Pi a una red ZeroTier:**

Después de la instalación, necesitas unir tu Raspberry Pi a una red ZeroTier existente. Para ello, necesitarás el **ID de red de 16 dígitos** de ZeroTier Central (my.zerotier.com).

Bash

sudo zerotier-cli join TU\_ID\_DE\_RED

Reemplaza TU\_ID\_DE\_RED con el ID de tu red ZeroTier.

**4. Autoriza tu dispositivo en ZeroTier Central:**

Una vez que tu Raspberry Pi intente unirse a la red, aparecerá como un nuevo miembro en la interfaz web de ZeroTier Central (my.zerotier.com). Debes iniciar sesión, ir a tu red y **marcar la casilla "Auth"** (autorizar) junto a la entrada de tu Raspberry Pi para permitirle acceder a la red.

**5. Comprueba el estado de ZeroTier (opcional):**

Para verificar que ZeroTier se está ejecutando correctamente, puedes usar:

Bash

sudo zerotier-cli status

Debería devolver algo como 200 info [ID] [versión] ONLINE.

**6. Habilita ZeroTier para que se inicie automáticamente (recomendado):**

Para asegurarte de que ZeroTier se inicie cada vez que tu Raspberry Pi arranque, habilita el servicio:

Bash

sudo systemctl enable zerotier-one

**Comandos adicionales de gestión:**

- **Iniciar el servicio ZeroTier:** 

  Bash

  sudo systemctl start zerotier-one

- **Detener el servicio ZeroTier:** 

  Bash

  sudo systemctl stop zerotier-one

- **Reiniciar el servicio ZeroTier:** 

  Bash

  sudo systemctl restart zerotier-one

- **Listar las redes a las que está unido:** 

  Bash

  sudo zerotier-cli listnetworks

¡Con estos pasos, tu Raspberry Pi 5 debería estar conectada a tu red ZeroTier!

