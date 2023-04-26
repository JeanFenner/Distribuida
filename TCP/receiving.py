import socket
import threading
def receive(IP, PORT):
    """
    Função para receber mensagens.
    """
    escuta_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    escuta_socket.bind((IP, PORT))
    escuta_socket.listen()

    while True:
        cliente, endereco = escuta_socket.accept()
        print("Conectado. Endereco: ", endereco, "\n")
        try:
            # Recebe a mensagem
            print("Teste")
#           message = cliente.recv(1024).decode("utf-8")
#           print(message)

            thread = threading.Thread(target=trata_cliente, args=(cliente,))
            thread.start()


        except:
            # Se houver erro na conexão, encerra a conexão
            escuta_socket.close()
            print("Erro na conexão")
            break

def trata_cliente(cliente):
    while True:
        message = cliente.recv(1024).decode("utf-8")
        print(message)