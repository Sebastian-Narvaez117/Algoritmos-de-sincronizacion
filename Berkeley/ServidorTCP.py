import socket
import time
from datetime import datetime

NODES = [
    "192.168.0.102",
    "192.168.0.103"
]

PORT = 6000

def format_time(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

times = []

my_time = time.time()

times.append(my_time)

print("\nMi hora local:")
print(format_time(my_time))

for ip in NODES:

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((ip, PORT))

        s.send(b"TIME")

        node_time = float(s.recv(1024).decode())

        times.append(node_time)

        print(f"\nNodo {ip}")
        print(f"Hora: {format_time(node_time)}")

        s.close()

    except Exception as e:

        print(f"Error con {ip}: {e}")

avg_time = sum(times) / len(times)

print("\n====================")
print("PROMEDIO CALCULADO")
print(format_time(avg_time))
print("====================")

for ip in NODES:

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((ip, PORT))

        msg = f"SET_TIME|{avg_time}"

        s.send(msg.encode())

        s.close()

        print(f"Ajuste enviado a {ip}")

    except Exception as e:

        print(e)

print("\nSincronización completada")