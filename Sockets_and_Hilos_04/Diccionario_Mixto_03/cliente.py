import socket, string, sys, os, time
clear = lambda: os.system('cls')

class Cliente():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(('127.0.0.1',9090))

        print("[Mix  dicctionary]")
        time.sleep(1)
        clear()

        while True:
            msj = input("[]: ")
            self.mi_socket.send(msj.encode())
            if(msj == 'cerrar'):
                break
            recbd=self.mi_socket.recv(1024)
            print(recbd.decode())

        print("hasta luego")
        self.mi_socket.close()

cliente = Cliente()
