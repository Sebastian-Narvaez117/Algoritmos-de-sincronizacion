# Algoritmos de Sincronización

Implementación de cuatro algoritmos clásicos de sincronización de relojes en sistemas distribuidos. Este proyecto contiene implementaciones en Python de los algoritmos **Berkeley**, **Cristian**, **Lamport** y **Vector Clock** utilizando protocolos **TCP** y **UDP**.

## Descripción de Algoritmos

### 1. **Algoritmo de Berkeley**
Algoritmo de sincronización donde un servidor maestro (administrador de tiempo) solicita la hora a todos los clientes, calcula el promedio y envía las correcciones necesarias.

- **Características:**
  - Servidor administrador centralizado
  - Cálculo de promedio de tiempos
  - Envío de correcciones a todos los clientes
  - Sincronización más rápida y eficiente

- **Archivos:**
  - `Berkeley/ServidorTCP.py` - Servidor maestro (TCP)
  - `Berkeley/ClienteTCP.py` - Cliente sincronizado (TCP)
  - `Berkeley/ServidorUDP.py` - Servidor maestro (UDP)
  - `Berkeley/ClienteUDP.py` - Cliente sincronizado (UDP)

---

### 2. **Algoritmo de Cristian**
Algoritmo donde cada cliente solicita la hora a un servidor de tiempo, incluyendo el tiempo de round-trip para mayor precisión.

- **Características:**
  - Comunicación cliente-servidor
  - Cálculo de latencia de red
  - Estimación del tiempo más precisa
  - Basado en RTT (Round-Trip Time)

- **Archivos:**
  - `Cristian/ServidorTCP.py` - Servidor de tiempo (TCP)
  - `Cristian/ClienteTCP.py` - Cliente que solicita sincronización (TCP)
  - `Cristian/ServidorUDP.py` - Servidor de tiempo (UDP)
  - `Cristian/ClienteUDP.py` - Cliente que solicita sincronización (UDP)

---

### 3. **Algoritmo de Lamport (Logical Clock)**
Implementación de relojes lógicos que mantienen un orden causal de eventos sin necesidad de sincronización de tiempo real.

- **Características:**
  - Orden causal garantizado
  - No requiere sincronización de reloj físico
  - Eventos distribuidos ordenados correctamente
  - Basado en contadores de eventos

- **Archivos:**
  - `Lamport/TCP.py` - Implementación con TCP
  - `Lamport/UDP.py` - Implementación con UDP

---

### 4. **Algoritmo de Vector Clock**
Extensión del reloj de Lamport que permite detectar relaciones de causalidad completas entre eventos en sistemas distribuidos.

- **Características:**
  - Detección de concurrencia
  - Orden parcial de eventos
  - Mejor precisión que Lamport
  - Vectores de relojes por nodo

- **Archivos:**
  - `Vector/ServidorTCP.py` - Servidor coordinador (TCP)
  - `Vector/ClienteTCP.py` - Cliente con clock vector (TCP)
  - `Vector/ServidorUDP.py` - Servidor coordinador (UDP)
  - `Vector/ClienteUDP.py` - Cliente con clock vector (UDP)

---

## Requisitos

- Python 3.7+
- Permisos de administrador (para ajustar hora del sistema)
- Redes locales para pruebas distribuidas

```bash
sudo apt-get install python3
```

---

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Sebastian-Narvaez117/Algoritmos-de-sincronizacion.git
cd Algoritmos-de-sincronizacion
```

2. (Opcional) Crear un entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

---

## Uso

### Ejecutar un algoritmo

Cada algoritmo tiene un servidor y clientes. Ejecuta primero el servidor:

```bash
# Ejemplo: Berkeley con TCP
cd Berkeley
sudo python3 ServidorTCP.py
```

En otra terminal, ejecuta el cliente:
```bash
cd Berkeley
sudo python3 ClienteTCP.py
```

### Protocolos disponibles

- **TCP**: Conexión orientada, más confiable
- **UDP**: Sin conexión, más rápido pero sin garantía de entrega

---

## Captura de Tráfico de Red

Se incluyen archivos `.pcapng` de Wireshark para cada algoritmo y protocolo, mostrando el análisis del tráfico de red generado durante la sincronización:

- `Berkeley/TCP Berkeley.pcapng` - Tráfico TCP del algoritmo Berkeley
- `Berkeley/UDP Berkeley.pcapng` - Tráfico UDP del algoritmo Berkeley
- `Cristian/TCP Cristian.pcapng` - Tráfico TCP del algoritmo Cristian
- `Cristian/UDP Cristian.pcapng` - Tráfico UDP del algoritmo Cristian
- `Lamport/TCP Lamport.pcapng` - Tráfico TCP del reloj de Lamport
- `Lamport/UDP Lamport.pcapng` - Tráfico UDP del reloj de Lamport
- `Vector/TCP Vector.pcapng` - Tráfico TCP del reloj Vector
- `Vector/UDP Vector.pcapng` - Tráfico UDP del reloj Vector

Para ver estas capturas, usa Wireshark:
```bash
wireshark archivo.pcapng
```

---

## Notas Importantes

- ⚠️ Requiere permisos de `sudo` para modificar la hora del sistema
- 🔒 Configura correctamente las direcciones IP según tu red local
- 🔌 Asegúrate de que los puertos estén disponibles
- 📊 Usa los archivos `.pcapng` para análisis detallado del tráfico

---

## Estructura del Proyecto

```
Algoritmos-de-sincronizacion/
├── Berkeley/
│   ├── ClienteTCP.py
│   ├── ClienteUDP.py
│   ├── ServidorTCP.py
│   ├── ServidorUDP.py
│   ├── TCP Berkeley.pcapng
│   └── UDP Berkeley.pcapng
├── Cristian/
│   ├── ClienteTCP.py
│   ├── ClienteUDP.py
│   ├── ServidorTCP.py
│   ├── ServidorUDP.py
│   ├── TCP Cristian.pcapng
│   └── UDP Cristian.pcapng
├── Lamport/
│   ├── TCP.py
│   ├── UDP.py
│   ├── TCP Lamport.pcapng
│   └── UDP Lamport.pcapng
├── Vector/
│   ├── ClienteTCP.py
│   ├── ClienteUDP.py
│   ├── ServidorTCP.py
│   ├── ServidorUDP.py
│   ├── TCP Vector.pcapng
│   └── UDP Vector.pcapng
└── README.md
```

---

## Autor

**Sebastián Narváez**

---

## Licencia

MIT