import socket
import threading

# Configuración fija de la red
MY_PORT = 7000
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

def receive():
    global logical_clock
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', MY_PORT))
    server.listen(5)
    
    while True:
        conn, addr = server.accept()
        data = conn.recv(1024).decode('utf-8')
        
        if data:
            received_clock, msg = data.split('|', 1)
            received_clock = int(received_clock)
            
            with reloj_lock:
                logical_clock = max(logical_clock, received_clock) + 1
        
                print("\r\033[K", end="") 
                print(f"[RECIBIDO de {addr[0]}] Reloj remoto: {received_clock} | Nuevo reloj local: {logical_clock}")
                print(f"Mensaje: {msg}\n")
                print("Mensaje: ", end="", flush=True)
        
        conn.close()

# Iniciar el hilo de recepción
threading.Thread(target=receive, daemon=True).start()

mi_ip = obtener_mi_ip()
mis_destinos = [ip for ip in TODAS_LAS_PCS if ip != mi_ip]

print("=========================================")
print("     CHAT DISTRIBUIDO TCP (LAMPORT)      ")
print(f"  Mi IP: {mi_ip} | Puerto: {MY_PORT}")
print(f"  Destinos: {mis_destinos}")
print("=========================================\n")

while True:
    msg = input("Mensaje: ")
    if not msg.strip(): continue

    with reloj_lock:
        logical_clock += 1
        packet = f"{logical_clock}|{msg}"
        print(f"[ENVÍO] Incremento mi reloj a: {logical_clock} y conectando...")

    for ip in mis_destinos:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1.0) 
            client.connect((ip, MY_PORT))
            client.sendall(packet.encode('utf-8'))
            client.close()
        except Exception:
            # Borrar la línea de carga si falla la conexión y mostrar el error limpio
            print(f" [Sistema] Nodo {ip} desconectado o no disponible")
            
    print("    Enviado correctamente.\n")