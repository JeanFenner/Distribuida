import socket
import threading
import time

# IDENTIFICACAO
ID = 2
IP = '127.0.0.102'
PORT = 5102

# DESTINO
ID_D = 1
IP_D = '127.0.0.101'
PORT_D = 5101

# CLIENTES
clients = []

# Recebe mensagens
def receive(IP, PORT):
    escuta_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    escuta_socket.bind((IP, PORT))
    escuta_socket.listen()

    while True:
        cliente, endereco = escuta_socket.accept()
        print("Conectado. Endereco: ", endereco, "\n")
        
        try:
            # Recebe a mensagem
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
        print("MENSAGEM: ", message)

# Envia mensagens
def envia_mensagem(message):
    for client in clients:
        client[0].send(message.encode("utf-8"))

def write():
    escreve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    escreve_socket.connect((IP_D, PORT_D))
    clients.append((escreve_socket, ID_D))

if __name__ == "__main__":
    print(ID, IP, PORT)

    receive_thread = threading.Thread(target=receive, args=(IP, PORT))
    receive_thread.start()

    print("Aguarde")
    time.sleep(10)
    
    write_thread = threading.Thread(target=write, args=())
    write_thread.start()

    while True:
        envia_mensagem(input())