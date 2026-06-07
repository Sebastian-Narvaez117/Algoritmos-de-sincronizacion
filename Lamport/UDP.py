import socket
import threading

# Configuración fija de la red
MY_PORT = 7001
ROUTER_IP = '192.168.0.1'
TODAS_LAS_PCS = ['192.168.0.101', '192.168.0.102', '192.168.0.103', '192.168.0.104']

logical_clock = 0
reloj_lock = threading.Lock()

def obtener_mi_ip():
    """Detecta automáticamente cuál de las 3 IPs de la red tiene esta máquina."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect((ROUTER_IP, 1))
        mi_ip = s.getsockname()[0]
    except Exception:
        mi_ip = '127.0.0.1'
    finally:
        s.close()
    return mi_ip

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', MY_PORT))

def receive():
    global logical_clock
    while True:
        data, addr = sock.recvfrom(1024)
        received_clock, msg = data.decode().split('|', 1)
        received_clock = int(received_clock)
        
        with reloj_lock:
            logical_clock = max(logical_clock, received_clock) + 1
            
            print("\r\033[K", end="") 
            print(f"[RECIBIDO de {addr[0]}] Reloj remoto: {received_clock} | Nuevo reloj local: {logical_clock}")
            print(f" Mensaje: {msg}\n")
            print("Mensaje: ", end="", flush=True)

# Iniciar el hilo de recepción
threading.Thread(target=receive, daemon=True).start()

mi_ip = obtener_mi_ip()
mis_destinos = [ip for ip in TODAS_LAS_PCS if ip != mi_ip]

print("=========================================")
print("     CHAT DISTRIBUIDO UDP (LAMPORT)      ")
print(f"  Mi IP: {mi_ip} | Puerto: {MY_PORT}")
print(f"  Destinos: {mis_destinos}")
print("=========================================\n")

while True:
    msg = input("Mensaje: ")
    if not msg.strip(): continue

    with reloj_lock:
        logical_clock += 1
        packet = f"{logical_clock}|{msg}"
        
        # Limpieza estética del envío
        print(f"[ENVÍO] Incremento mi reloj a: {logical_clock} y envío a todos...")

    for ip in mis_destinos:
        try:
            sock.sendto(packet.encode(), (ip, MY_PORT))
        except Exception:
            print(f" [Error] No se pudo enviar por UDP a {ip}")
            
    print("    Enviado correctamente.\n")