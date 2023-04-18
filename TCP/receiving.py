import socket

def receive(IP, PORT):
    """
    Função para receber mensagens.
    """
    escuta_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    escuta_socket.bind((IP, PORT))
    escuta_socket.listen()

    while True:
        cliente = escuta_socket.accept()
        print("Conectado. Endereco: ", cliente[1], "\n")
        try:
            # Recebe a mensagem
            message = escuta_socket.recv(1024).decode("utf-8")
            print(message)
        except:
            # Se houver erro na conexão, encerra a conexão
            escuta_socket.close()
            break
