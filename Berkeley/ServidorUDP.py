import socket
import time
from datetime import datetime

NODES = [
    "192.168.0.102",
    "192.168.0.103"
]

PORT = 6001

def format_time(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(5)

times = [time.time()]

print("Mi hora:", format_time(times[0]))

# Enviar TIME a todos
for ip in NODES:
    print(f"Solicitando hora a {ip}")
    sock.sendto(b"TIME", (ip, PORT))

# Recibir respuestas
respuestas = 0

while respuestas < len(NODES):

    try:

        data, addr = sock.recvfrom(1024)

        node_time = float(data.decode())

        print(f"Respuesta de {addr[0]} -> {format_time(node_time)}")

        times.append(node_time)

        respuestas += 1

    except socket.timeout:

        print("Timeout esperando respuestas")
        break

avg_time = sum(times) / len(times)

print("\nPromedio:", format_time(avg_time))

# Enviar ajuste
for ip in NODES:

    msg = f"SET_TIME|{avg_time}"

    sock.sendto(msg.encode(), (ip, PORT))

    print(f"Ajuste enviado a {ip}")

print("\nSincronización finalizada")