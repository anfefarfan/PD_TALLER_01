import socket
import threading
import sys
import DB

DB.CREATE_DB("python_db")
DB.CREATE_TABLE("chat_history", "message")

class Servidor():
    def __init__(self, host="localhost", puerto=9999):
        self.clients = []
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
        print("chat start")
        while True:
            try:
                conection, direccion = self.sock.accept()
                conection.setblocking(False)
                self.clients.append(conection)
            except:
                pass

    def proceso_conectiones(self):
        print("proceso conection")
        while True:
            if len(self.clients) > 0:
                for client in self.clients:
                    try:
                        date = client.recv(1024)
                        if date:
                            self.msj_todos(date, client)
                    except:
                        pass

    def msj_todos(self, msj, client):
        DB.INSERT_DB("chat_history", "message", msj.decode())
        for c in self.clients:
            try:
                if c != client:
                    c.send(msj)
            except:
                self.clients.remove(client)

servidor = Servidor()
