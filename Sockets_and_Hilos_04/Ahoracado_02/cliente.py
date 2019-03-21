import socket, string, sys, os, time
clear = lambda: os.system('cls')

class Cliente():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(('127.0.0.1',9090))

        print("    [AHORCADO]")
        time.sleep(1)
        print("\t ______\n\t |    |\n\t      |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n")

        while True:
            mensaje = input("[]: ")
            self.mi_socket.send(mensaje.encode())
            if(mensaje == 'cerrar'):
                break
            clear()
            print("    [JUEGO AHORCADO]")
            recibido = self.mi_socket.recv(1024)
            print(recibido.decode())

        print("adios")
        self.mi_socket.close()


cliente = Cliente()
