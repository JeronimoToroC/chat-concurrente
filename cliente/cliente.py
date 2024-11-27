import socket
import threading

# Configuración del servidor al que conectarse
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345        # Puerto del servidor

def conectar_al_servidor():
    """Establece la conexión con el servidor."""
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    # Solicitar y enviar alias
    alias = input("Ingresa tu alias: ")
    cliente.sendall(alias.encode('utf-8'))

    print(f"Conectado al servidor {HOST}:{PORT}")

    # Crear un hilo para recibir mensajes
    hilo_receptor = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_receptor.start()

    # Manejar el envío de mensajes
    enviar_mensajes(cliente)

def recibir_mensajes(cliente):
    """Recibe mensajes del servidor y los muestra."""
    try:
        while True:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje:
                print(f"\n{mensaje}")
            else:
                break
    except ConnectionResetError:
        print("Conexión cerrada por el servidor.")
    finally:
        cliente.close()

def enviar_mensajes(cliente):
    """Permite al usuario enviar mensajes al servidor."""
    try:
        while True:
            mensaje = input("Tú: ")
            if mensaje.lower() == "salir":
                print("Desconectando del servidor...")
                cliente.close()
                break
            cliente.sendall(mensaje.encode('utf-8'))
    except BrokenPipeError:
        print("No se pudo enviar el mensaje. El servidor está desconectado.")

if __name__ == "__main__":
    conectar_al_servidor()
