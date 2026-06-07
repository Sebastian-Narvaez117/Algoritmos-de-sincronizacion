import socket
import time
import subprocess
from datetime import datetime

SERVER_IP = "192.168.0.102"   #Direccion estatica del servidor dentro de la red local
PORT = 5001

def set_system_time(timestamp):        #Función para actualizar la hora del sistema utilizando timedatectl
    fecha = datetime.fromtimestamp(timestamp)
    fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
    print("Nodo cliente: Cristian UDP activo")
    print("Hora actual del sistema:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Hora recibida del servidor:", fecha_str)
    subprocess.run([
        "sudo",
        "timedatectl",
        "set-time",
        fecha_str
    ])

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"\nConexion establecida con el servidor {SERVER_IP}:{PORT}...")

t1 = time.time()
client.sendto(b"TIME", (SERVER_IP, PORT))
data, _ = client.recvfrom(1024)
t3 = time.time()                    #Tiempo de recepción del mensaje del servidor para calcular el RTT y el delay
t2 = float(data.decode())
RTT = t3 - t1
delay = RTT / 2
new_time = t2 + delay

print("========= CRISTIAN UDP =========")
set_system_time(new_time)
print("Hora actualizada del sistema:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("================================")
client.close()
