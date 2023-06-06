import socket
import threading
import time

# SALDO
global saldo
saldo = float(1000.00)

# TEMPO RELATIVO
global tr
tr = int(1)

# FILAS
msgs = []
msg_ack = []

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
    global tr
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
    global tr
    while True:
        message = cliente.recv(1024).decode("utf-8")
        tratar_mensagem(message)
        tr += 1

def get_message(msg):
        print("\t",msg)
        op, trid = str(msg).replace('\n','').split(',')
        trid.replace(' ','')
        trid = float(trid)
        return (op, trid)

def tratar_mensagem(msg):
    global saldo
    global msgs

    print(msg)
    if str(msg).count("ACK"):
#        msg_str = str(msg).replace('\n','').split('_')[1]
#        print("STR",msg_str)
#        message = get_message(msg_str.replace("('",'').replace("'",'').replace(")",''))
#        for m in msg_ack:
#            print(m)
#            if message == m[0]:
#                print("SIM")
        print("ACK")
    else:
        message = get_message(msg)
        msgs.append(message)
        msgs.sort(key=lambda x:x[1])
        msg_ack.append((message, int(0)))
        if message[0] == 'D100':
            saldo += 100
        elif message[0] == 'J1':
            saldo += saldo*.01
        print(saldo)

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

# Envia confirmações
def confirm():
    global tr
    while True:
        time.sleep(5)

        if len(msgs)>0:
            print("msgs: ",msgs)
            msg = msgs.pop(0)
            tr_msg = int(msg[1])
            id_msg = int((msg[1]%1)*10)
            
            if id_msg <= ID:
                envia_mensagem("ACK_"+str(msg))
            elif tr_msg <= tr:
                envia_mensagem("ACK_"+str(msg))
        
#        if len(msg_ack)>0:
#            msg = msg_ack[0]
#            if msg[1] == len(clients):
#                if msg[0] == 'D100':
#                    saldo += 100
#                elif msg[0] == 'J1':
#                    saldo += saldo*.01
#                print(saldo)

# Le endereços
def get_addrs():
    for address in addrs_file:
        address = address.replace("\n","").split(";")
        addrs.append((int(address[0]), address[1], int(address[2])))

# Envia operações
def operacao(op):
    global tr
    if op == 1:
        envia_mensagem("D100,"+str(tr)+'.'+str(ID))
    elif op == 2:
        envia_mensagem("J1,"+str(tr)+'.'+str(ID))
    elif op == 0:
        print(saldo,"\n")
    else:
        print("Invalido")

    tr += 1

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

    ack_thread = threading.Thread(target=confirm, args=())
    ack_thread.start()

    op = 0
    while True:
        print("TR=",tr,"\n[1] - Depositar 100\n[2] - Juros 1%\n[0] - Saldo\n")
        op = int(input())
        operacao(op)
