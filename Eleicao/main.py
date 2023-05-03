import socket
import threading

# ARQUIVO
addrs_file = open("addrs.txt", "r")
addrs = []

# IDENTIFICACAO
ID = 0
IP = ''
PORT = 0

# ENDERECOS
clients = []
nao_clients = []

#
#   ENVIA MENSAGENS
#

def envia_mensagem(message):
    for client in clients:
        client.send(message.encode("utf-8"))

def write(id, addrs):
    """
    Função para enviar mensagens.
    """
    
    for address in addrs:
        if(address[0] != addrs[id-1][0]):
            escreve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                escreve_socket.connect((address[1], address[2]))
                clients.append(escreve_socket)
            except:
               nao_clients.append(address)

    while True:
        message = input()
        # Envia a mensagem
        envia_mensagem(message)

#
#   RECEBE MENSAGENS
#

def receive(IP, PORT):
    """
    Função para receber mensagens.
    """
    escuta_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    escuta_socket.bind((IP, PORT))
    escuta_socket.listen()

    while True:
        cliente, endereco = escuta_socket.accept()
        try:
            # Recebe a mensagem
            print("Conectado. Endereco: ", endereco, "\n")

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

def get_addrs():
    for address in addrs_file:
        address = address.replace("\n","").split(";")
        addrs.append((int(address[0]), address[1], int(address[2])))

#
#   INICIO
#

if __name__ == "__main__":
    get_addrs()

    print(addrs)

    print("Escolha seu ID(1-5): ")
    ID = int(input())
    IP, PORT = addrs[ID-1][1], addrs[ID-1][2]

    print(ID, IP, PORT)
    
    # Inicia duas threads, uma para receber mensagens do servidor e outra para enviar mensagens para o servidor.
    receive_thread = threading.Thread(target=receive, args=(IP, PORT))
    receive_thread.start()

    ok = input()
    print(ok)
    
    write_thread = threading.Thread(target=write, args=(ID, addrs))
    write_thread.start()