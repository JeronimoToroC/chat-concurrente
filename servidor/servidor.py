import socket
import threading
import logging

# Configuración de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("servidor/logs/chat.log"), logging.StreamHandler()]
)

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP local
PORT = 12345        # Puerto para escuchar conexiones

# Lista para almacenar clientes conectados
clientes = []
# Almacena los clientes y sus alias
clientes_alias = {}

def iniciar_servidor():
    """Inicializa el servidor y escucha nuevas conexiones."""
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(5)  # Máximo 5 conexiones en cola
    logging.info(f"Servidor iniciado en {HOST}:{PORT}")

    try:
        while True:
            cliente_socket, cliente_direccion = servidor.accept()
            logging.info(f"Conexión recibida de {cliente_direccion}")

            # Crear un hilo para manejar al cliente
            hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
            hilo_cliente.start()
            clientes.append(cliente_socket)
    except KeyboardInterrupt:
        cerrar_servidor(servidor)

def manejar_cliente(cliente_socket):
    """Maneja la comunicación con un cliente."""
    try:
        # Solicitar alias
        cliente_socket.sendall("Por favor, ingresa tu alias: ".encode('utf-8'))
        alias = cliente_socket.recv(1024).decode('utf-8')
        clientes_alias[cliente_socket] = alias
        logging.info(f"Alias recibido: {alias}")
        enviar_a_todos(f"{alias} se ha unido al chat.")

        while True:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            if not mensaje:
                break
            mensaje_con_alias = f"{alias}: {mensaje}"
            logging.info(f"Mensaje recibido: {mensaje_con_alias}")
            enviar_a_todos(mensaje_con_alias, cliente_socket)
    except ConnectionResetError:
        logging.warning("Conexión perdida con un cliente.")
    finally:
        alias = clientes_alias.pop(cliente_socket, "Un cliente")
        clientes.remove(cliente_socket)
        cliente_socket.close()
        enviar_a_todos(f"{alias} ha salido del chat.")

def enviar_a_todos(mensaje, emisor=None):
    """Envía un mensaje a todos los clientes excepto al emisor (opcional)."""
    for cliente in clientes:
        if cliente != emisor:
            cliente.sendall(mensaje.encode('utf-8'))

def cerrar_servidor(servidor):
    """Detiene el servidor y cierra conexiones activas."""
    logging.info("Cerrando servidor...")
    servidor.close()
    for cliente in clientes:
        cliente.close()
    logging.info("Servidor cerrado.")

if __name__ == "__main__":
    iniciar_servidor()
