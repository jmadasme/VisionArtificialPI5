import socket
import ipaddress
import concurrent.futures

# Configura aquí tu red local, por ejemplo '192.168.1.0/24'
RED_LOCAL = '192.168.100.0/24'
PUERTO_SSH = 22
TIEMPO_ESPERA = 1  # segundos

def escanear_ip(ip):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIEMPO_ESPERA)
            resultado = sock.connect_ex((str(ip), PUERTO_SSH))
            if resultado == 0:
                return str(ip)
    except Exception:
        pass
    return None


def escanear_red(red):
    red_ips = ipaddress.ip_network(red).hosts()
    print(f"Escaneando la red {red} en busca de servicios SSH...\n")

    encontrados = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        resultados = executor.map(escanear_ip, red_ips)
        for ip in resultados:
            if ip:
                print(f"[✔] SSH detectado en {ip}")
                encontrados.append(ip)

    if not encontrados:
        print("\nNo se encontraron servicios SSH en la red.")
    else:
        print(f"\nTotal encontrados: {len(encontrados)}")


if __name__ == "__main__":
    escanear_red(RED_LOCAL)
