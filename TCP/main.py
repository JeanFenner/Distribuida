import threading
import receiving
import sending

adrs_file = open("addrs.txt", "r")
addrs = []
ID = 0
IP = ''
PORT = 0

def get_addrs():
    for x in adrs_file:
        x = x.replace("\n","").split(";")
        addrs.append((int(x[0]), x[1], int(x[2])))

if __name__ == "__main__":
    get_addrs()

    print(addrs)

    print("Escolha seu ID(1-5): ")
    ID = int(input())
    IP, PORT = addrs[ID-1][1], addrs[ID-1][2]

    print(ID, IP, PORT)
    

    # Inicia duas threads, uma para receber mensagens do servidor e outra para enviar mensagens para o servidor.
    receive_thread = threading.Thread(target=receiving.receive, args=(IP, PORT))
    receive_thread.start()

#    ok = input()
#    print(ok)
    
#    write_thread = threading.Thread(target=sending.write, args=(IP_S, PORT_S))
#    write_thread.start()
