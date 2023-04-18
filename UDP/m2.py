import threading
import receiving
import sending

# Endereço IP e porta do servidor
IP_R = "127.0.0.20"
PORT_R = 5002
IP_S = "127.0.0.10"
PORT_S = 5001

if __name__ == "__main__":
    # Inicia duas threads, uma para receber mensagens do servidor e outra para enviar mensagens para o servidor.
    receive_thread = threading.Thread(target=receiving.receive, args=(IP_R, PORT_R))
    receive_thread.start()

    ok = input()
    print(ok)
    
    write_thread = threading.Thread(target=sending.write, args=(IP_S, PORT_S))
    write_thread.start()