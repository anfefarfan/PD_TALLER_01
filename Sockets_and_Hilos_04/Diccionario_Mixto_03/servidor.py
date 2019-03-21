import socket, diccionario

class Servidor():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conection, direcction = self.mi_socket.accept()

        while True:
            msj = conection.recv(1024)
            print("[]: "+msj.decode())

            msj = diccionario.traducir(msj.decode())

            conection.send("[MIXTO]: ".encode() + str(msj).encode())

        print("close")
        conection.close()
        self.mi_socket.close()

servidor = Servidor()
