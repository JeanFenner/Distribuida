import socket

def write(IP, PORT):
    """
    Função para enviar mensagens.
    """
    escreve_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:

        message = input()
        # Envia a mensagem
        escreve_socket.sendto(message.encode("utf-8"), (IP, PORT))