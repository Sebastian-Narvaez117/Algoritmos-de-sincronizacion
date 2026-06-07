import socket
import time
import subprocess
from datetime import datetime

HOST = "0.0.0.0"
PORT = 6000

def format_time(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def set_system_time(timestamp):

    fecha = datetime.fromtimestamp(timestamp)

    fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")

    subprocess.run([
        "sudo",
        "timedatectl",
        "set-time",
        fecha_str
    ])

    print(f"\nHora actualizada a: {fecha_str}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print(f"Esclavo Berkeley TCP escuchando puerto {PORT}")

while True:

    conn, addr = server.accept()

    data = conn.recv(1024).decode()

    if data == "TIME":

        current_time = time.time()

        print(f"\nSolicitud TIME desde {addr}")

        conn.send(str(current_time).encode())

    elif data.startswith("SET_TIME"):

        timestamp = float(data.split("|")[1])

        print("\nAjuste recibido")

        print("Nueva hora:", format_time(timestamp))

        set_system_time(timestamp)

    conn.close()