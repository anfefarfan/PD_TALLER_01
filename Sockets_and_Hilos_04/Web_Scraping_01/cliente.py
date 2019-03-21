import threading, socket, sys

class Cliente():
    def __init__(self, host="localhost", port=9090):
        self.sock = socket.socket()
        self.sock.connect((host, port))

        msj_server = threading.Thread(target=self.msj_ser)
        msj_server.setDaemon = True
        msj_server.start()

        url = input("\nOpciones:\n\n"
                        "1. Webscraping YOUTUBE.\n"
                        "2. Salir.\n\n"
                    "Elige una opcion: ")

        while True:
            self.enviar_msj(url)
            url = ""

    def msj_ser(self):
        try:
            data = self.sock.recv(1024)
            if data:
                print("Resultado: ",data.decode())
        except:
            print("Error")
            self.sock.close()
            sys.exit()

    def enviar_msj(self, url):
        self.sock.send(url.encode())

client = Cliente()
