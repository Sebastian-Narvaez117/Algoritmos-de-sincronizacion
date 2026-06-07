import socket
import threading
import ast
from datetime import datetime

HOST = '0.0.0.0'
PORT = 8001

vector = [0,0,0]

MY_INDEX = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print(f"""
==============================
 SERVIDOR VECTOR TCP
 IP: {HOST}
 PORT: {PORT}
==============================
""")

def handle_client(conn, addr):

    global vector

    print(f"\nCliente conectado: {addr}")

    while True:

        data = conn.recv(1024)

        if not data:
            break

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

    conn.close()

while True:

    conn, addr = server.accept()

    thread = threading.Thread(target=handle_client, args=(conn, addr))

    thread.start()