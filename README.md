# Chat con Sockets y Programación Concurrente

Este proyecto implementa un sistema de chat simple que permite la comunicación entre múltiples clientes mediante sockets en Python. Se utiliza programación concurrente para manejar múltiples conexiones al mismo tiempo.

---

## Características

- **Comunicación en tiempo real**: Los clientes pueden enviar y recibir mensajes de forma simultánea.
- **Identificación de usuarios**: Cada cliente puede ingresar un alias único para identificarse en el chat.
- **Notificaciones de conexión/desconexión**: Los clientes son notificados cuando otros se conectan o desconectan.
- **Soporte para múltiples clientes**: El servidor puede manejar varias conexiones concurrentes.

---

## Estructura del Proyecto

```
chat-proyecto/
│
├── servidor/
│   ├── servidor.py           # Código principal del servidor.
│   ├── logs/
│       └── chat.log          # Registro de eventos del servidor.
│
├── cliente/
│   ├── cliente.py            # Código principal del cliente.
│
├── README.md                 # Documentación del proyecto.
```

---

## Requisitos

- Python 3.8 o superior.
- Módulos estándar: `socket`, `threading`, `logging`.

---

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/chat-proyecto.git
   cd chat-proyecto
   ```

2. Asegúrate de que el entorno tenga Python 3 instalado.

---

## Uso

### 1. Iniciar el Servidor

Ejecuta el servidor desde la carpeta `servidor`:

```bash
python servidor/servidor.py
```

### 2. Conectar Clientes

Ejecuta el cliente desde la carpeta `cliente`. Repite esto en terminales separadas para múltiples usuarios:

```bash
python cliente/cliente.py
```

### 3. Interactuar en el Chat

- Ingresa un alias cuando se te solicite.
- Escribe mensajes para enviarlos a todos los demás usuarios conectados.
- Usa el comando `salir` para desconectarte del chat.

---

## Ejemplo

### Usuario 1

```bash
Ingresa tu alias: Usuario1
Tú: Hola, ¿cómo están?
```

### Usuario 2

```bash
Ingresa tu alias: Usuario2
Mensaje recibido: Usuario1: Hola, ¿cómo están?
Tú: Todo bien, gracias.
```

### Notificación de desconexión

```bash
Usuario1 ha salido del chat.
```

---

## Funcionalidades Futuras

- Soporte para mensajes privados.
- Almacenamiento del historial del chat.
- Implementación de una interfaz gráfica.

---

## Contribución

Si deseas contribuir, abre un **issue** o crea un **pull request**.

---

## Contacto

Creado por: Jerónimo Toro C
Correo: jeronimo.toro.c@gmail.com
