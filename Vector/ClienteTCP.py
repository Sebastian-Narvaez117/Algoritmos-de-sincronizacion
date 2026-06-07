# ==============================
# CLIENTE - P2 O P3
# ==============================

import socket
import json
import time
from datetime import datetime

SERVER_IP = "192.168.0.102"
PORT = 8001

# Cada cliente tiene SU vector
vector = [0,0,0]

# P2 = 1
# P3 = 2
MY_INDEX = int(input("Indice (1=P2, 2=P3): "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, PORT))

print(f"""
==============================
 CONECTADO AL SERVIDOR
==============================
Servidor: {SERVER_IP}:{PORT}
Mi indice: {MY_INDEX}
==============================
""")

while True:

    msg = input("\nMensaje: ")

    # Evento interno/envio
    vector[MY_INDEX] += 1

    packet = {

        "vector": vector,
        "msg": msg

    }

    current = datetime.now().strftime('%H:%M:%S.%f')[:-3]

    client.send(
        json.dumps(packet).encode()
    )

    print(f"""
======= VECTOR ENVIADO =======

Hora:
{current}

Mensaje:
{msg}

Vector enviado:
{vector}

================================
""")

    time.sleep(1)