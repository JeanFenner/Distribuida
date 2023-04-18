import threading
import socket

# Endereço IP e porta do servidor
IP_R = "127.0.0.30"
PORT_R = 5003
IP_S = "127.0.0.10"
PORT_S = 5001

def receive():
    """
    Função para receber mensagens.
    """
    escuta_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    escuta_socket.bind((IP_R, PORT_R))

    while True:
        # Recebe a mensagem
        message = escuta_socket.recv(1024).decode("utf-8")
        if message:
            print(message)

def write():
    """
    Função para enviar mensagens.
    """
    escreve_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:

        msg = input()
        message = msg + "<" + IP_R + ">"
        # Envia a mensagem
        escreve_socket.sendto(message.encode("utf-8"), (IP_S, PORT_S))

if __name__ == "__main__":
    # Inicia duas threads, uma para receber mensagens do servidor e outra para enviar mensagens para o servidor.
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    
    write_thread = threading.Thread(target=write)
    write_thread.start()
