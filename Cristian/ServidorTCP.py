import socket
import time

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor Cristian TCP iniciado")
print(f"""
==============================
 SERVIDOR CRISTIAN TCP
 IP: {HOST}
 PORT: {PORT}
==============================
""")

while True:

    conn, addr = server.accept()
    print(f"\nNodo cliente: Cristian activo")
    print(f"\nConexión establecida con: {addr}")

    t2 = time.time()

    print(f"Hora enviada: {time.ctime(t2)}")

    conn.send(str(t2).encode())

    print(f"Conexión cerrada con: {addr}")

    conn.close()