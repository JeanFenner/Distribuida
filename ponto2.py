import socket
import threading

# Endereço IP e porta do servidor
IP = "127.0.0.20"
PORT = 5002
client_add = "127.0.0.10"
client_port = 5001

# Iniciando o socket do cliente
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive():
    """
    Função para receber mensagens do servidor.
    """

    c, a = server_socket.accept()

    while True:
        try:
            # Recebe a mensagem do servidor
            message = server_socket.recv(1024).decode("utf-8")
            print(message)
            print(message)
            f = open("ponto2.txt", "w")
            print(message, file=f)
        except:
            # Se houver erro na conexão, encerra a conexão
            server_socket.close()
            c.close()
            break

def write():
    client_socket.connect((client_add, client_port))
    """
    Função para enviar mensagens para o servidor.
    """
    while True:
        message = input()
        # Envia a mensagem para o servidor
        client_socket.send(message.encode("utf-8"))

if __name__ == "__main__":
    # Inicia duas threads, uma para receber mensagens do servidor e outra para enviar mensagens para o servidor.
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    print("Conectar?")
    m = input()

    write_thread = threading.Thread(target=write)
    write_thread.start()