import socket
import time
import subprocess
from datetime import datetime

HOST = "0.0.0.0"
PORT = 6001

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

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print(f"Esclavo Berkeley UDP escuchando puerto {PORT}")

while True:

    data, addr = server.recvfrom(1024)

    msg = data.decode()

    if msg == "TIME":

        current_time = time.time()

        print(f"\nSolicitud TIME desde {addr}")

        server.sendto(str(current_time).encode(), addr)

    elif msg.startswith("SET_TIME"):

        timestamp = float(msg.split("|")[1])

        print("\nAjuste recibido")

        print("Nueva hora:", format_time(timestamp))

        set_system_time(timestamp)