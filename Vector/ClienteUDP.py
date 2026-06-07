import socket
from datetime import datetime

SERVER_IP = "192.168.0.102"

PORT = 8000

vector = [0,0,0]

MY_INDEX = 1

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"\nConectado a {SERVER_IP}:{PORT}")

while True:

    msg = input("\nMensaje: ")

    vector[MY_INDEX] += 1

    current = datetime.now().strftime('%H:%M:%S.%f')[:-3]

    packet = f"{vector}|{msg}"

    client.sendto(packet.encode(), (SERVER_IP, PORT))

    print(f"""
======= VECTOR ENVIADO =======

Hora local:
{current}

Mensaje:
{msg}

Vector enviado:
{vector}

================================
""")
    print("Cerrando conexión...")
    client.close()