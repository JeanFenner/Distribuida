import socket
import threading
import time

# ARQUIVO
addrs_file = open("addrs.txt", "r")
addrs = []

# IDENTIFICACAO
ID = 0
IP = ''
PORT = 0

# CLIENTES
clients = []
nao_clients = []

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
    for address in addrs:
        escreve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            escreve_socket.connect((address[1], address[2]))
            clients.append((escreve_socket, address[0]))
        except:
            nao_clients.append(address)

# Le endereços
def get_addrs():
    for address in addrs_file:
        address = address.replace("\n","").split(";")
        addrs.append((int(address[0]), address[1], int(address[2])))


if __name__ == "__main__":
    get_addrs()

    print(addrs)

    print("Escolha seu ID(1-5): ")
    ID = int(input())
    IP, PORT = addrs[ID-1][1], addrs[ID-1][2]

    print(ID, IP, PORT)

    receive_thread = threading.Thread(target=receive, args=(IP, PORT))
    receive_thread.start()

    ok = input()
    print(ok)
    
    write_thread = threading.Thread(target=write, args=())
    write_thread.start()

    op = 0
    while True:
        envia_mensagem(input())