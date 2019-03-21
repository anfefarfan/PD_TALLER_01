import socket
import threading
import sys

class Servidor():
    def __init__(self, host="localhost", puerto=9999):
        self.clientes = []
        self.sock = socket.socket()
        self.sock.bind((host, puerto))
        self.sock.listen(10)

        self.sock.setblocking(False)

        acept = threading.Thread(target=self.acept_conectiones)
        proceso = threading.Thread(target=self.proceso_conectiones)

        acept.start()
        proceso.start()

        try:
            while True:
                msj = input(">>")
                if msj == 'salir':
                    self.sock.close()
                    sys.exit()

        except:
            self.sock.close()
            sys.exit()

    def acept_conectiones(self):
        print("chat iniciado")
        while True:
            try:
                conection, direction = self.sock.accept()
                conection.setblocking(False)
                self.clientes.append(conection)
            except:
                pass

    def proceso_conectiones(self):
        print("proceso conection")
        while True:
            if len(self.clientes) > 0:
                for cliente in self.clientes:
                    try:
                        datos = cliente.recv(1024)
                        if datos:
                            self.msj_todos(datos, cliente)
                    except:
                        pass

    def msj_todos(self, msj, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msj)
            except:
                self.clientes.remove(cliente)

servidor = Servidor()
