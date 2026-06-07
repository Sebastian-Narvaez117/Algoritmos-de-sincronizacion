import socket
import time

HOST = "0.0.0.0"
PORT = 5001
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("Servidor Cristian UDP iniciado")
print(f"""
==============================
 SERVIDOR CRISTIAN UDP
 IP: {HOST}
 PORT: {PORT}
==============================
""")
while True:

    data, addr = server.recvfrom(1024)
    print(f"\nConexión establecida con: {addr}")
    print(f"\nMensaje recibido desde: {addr}")

    t2 = time.time()
    print(f"Hora enviada: {time.ctime(t2)}")

    server.sendto(str(t2).encode(), addr)

    print(f"Conexión cerrada con: {addr}")