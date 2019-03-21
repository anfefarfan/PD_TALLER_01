import socket, threading, sys, os, time

class Cliente():
    def __init__(self, host="localhost", puerto=9999):
        clear = lambda: os.system('cls')
        
        self.sock = socket.socket()
        self.sock.connect((host, puerto))

        msj_servidor = threading.Thread(target=self.msj_server)
        msj_servidor.setDaemon(True)
        msj_servidor.start()

        global nombre
        nombre = input("Ingrese su nombre: ")
        print("{{recibido}}")
        time.sleep(.500)

        clear()

        while True:
            msj = input()
            if msj !='salir':
                self.enviar_msj("["+nombre+"]: "+msj)
            else:
                self.sock.close()
                sys.exit()

    def msj_server(self):
        while True:
            try:
                datos = self.sock.recv(1024)
                if datos:
                    print(datos.decode())
            except:
                pass

    def enviar_msj(self, msj):
        self.sock.send(msj.encode())

cliente = Cliente()

#
#
# import socket
# import threading
# import sys
#
# class Cliente():
#     def __init__(self, host="localhost", puerto=9999):
#         self.sock = socket.socket()
#         self.sock.connect((host, puerto))
#
#         msj_servidor = threading.Thread(target=self.msj_server)
#         msj_servidor.setDaemon(True)
#         msj_servidor.start()
#
#         while True:
#             msj = input(">>")
#             if msj !='salir':
#                 self.enviar_msj(msj)
#             else:
#                 self.sock.close()
#                 sys.exit()
#
#     def msj_server(self):
#         while True:
#             try:
#                 datos = self.sock.recv(1024)
#                 if datos:
#                     print(datos.decode())
#             except:
#                 pass
#
#     def enviar_msj(self, msj):
#         self.sock.send(msj.encode())
#
# cliente = Cliente()
