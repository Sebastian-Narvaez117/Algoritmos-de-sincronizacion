import socket
import ast
from datetime import datetime

HOST = '0.0.0.0'
PORT = 8000

vector = [0,0,0]

MY_INDEX = 0

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print(f"""
==============================
 SERVIDOR VECTOR UDP
 IP: {HOST}
 PORT: {PORT}
==============================
""")

while True:

    data, addr = server.recvfrom(1024)

    recv_vector, msg = data.decode().split('|')

    recv_vector = ast.literal_eval(recv_vector)

    for i in range(3):
        vector[i] = max(vector[i], recv_vector[i])

    vector[MY_INDEX] += 1

    current = datetime.now().strftime('%H:%M:%S.%f')[:-3]

    print(f"""
======= VECTOR CLOCK =======

Hora local:
{current}

IP origen:
{addr[0]}

Mensaje:
{msg}

Vector recibido:
{recv_vector}

Vector actualizado:
{vector}

============================
""")
