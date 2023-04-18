import socket

def receive(IP, PORT):
    """
    Função para receber mensagens.
    """
    escuta_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    escuta_socket.bind((IP, PORT))

    while True:
        # Recebe a mensagem
        message = escuta_socket.recv(1024).decode("utf-8")
        print(message)
