import socket

class Servidor():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()

        global nom
        nom = conexion.recv(1024)
        conexion.send("{{nombre aceptado}}".encode())

        while True:
            msj = conexion.recv(1024)
            print("["+nom.decode()+"]: "+msj.decode())
            conexion.send("{{recibido}}".encode())
            if(msj.decode()== 'cerrar'):
                break
        print("close")
        conexion.close()
        self.mi_socket.close()

servidor = Servidor()
