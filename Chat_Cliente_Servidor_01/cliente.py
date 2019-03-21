import socket, string, sys, os, time
clear = lambda: os.system('cls')

class Cliente():

    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(('127.0.0.1',9090))

        global nom
        nom = input("Ingrese su nombre: ")
        self.mi_socket.send(nom.encode())
        recibido=self.mi_socket.recv(1024)
        print(recibido.decode())
        time.sleep(.500)

        clear()

        while True:
            msj = input("["+nom+"]: ")
            self.mi_socket.send(msj.encode())
            if(msj == 'cerrar'):
                break
            recibido=self.mi_socket.recv(1024)
            print(recibido.decode())

        print("hasta luego")
        self.mi_socket.close()

cliente = Cliente()
