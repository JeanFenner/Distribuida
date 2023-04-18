import socket

def write(IP, PORT):
    """
    Função para enviar mensagens.
    """
    escreve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    escreve_socket.connect((IP, PORT))
    while True:
        message = input()
        # Envia a mensagem
        escreve_socket.send(message.encode("utf-8"))